import plotly.express as px
import plotly.graph_objects as go

from meta.util import setup
from meta.config import config

monster_data, challenge_rating, hit_points, armor_class = setup()

fig = go.Figure()
for stat in config.get("stats"):
    fig.add_trace(
        # if we didn't have multiple series here,
        # you could just pass in the data frame + column names
        go.Scatter(
            x=challenge_rating,
            y=monster_data[stat],
            mode="markers",
            marker=dict(size=hit_points / 10),  # no automatic min/max size :()
            name=stat,
            hovertext=monster_data["name"],  # some lovely interactivity
            hoverinfo="text",
        )
    )

# add title and labels
fig.update_layout(
    title=config.get("chart_title"),
    xaxis_title=config.get("x_axis"),
    yaxis_title=config.get("y_axis"),
    legend_title="Stats",
)

# add our little note
fig.add_annotation(
    x=0,
    y=max(monster_data["strength"]),
    showarrow=False,
    yshift=10,
    text=config.get("blurb"),
)

# show the chart
fig.show()

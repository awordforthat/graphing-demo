from bokeh.plotting import figure, show
from bokeh.models import Label

from meta.util import setup
from meta.config import config

monster_data, challenge_rating, hit_points, armor_class = setup()

# for some reason, bokeh doesn't automatically assign
# unique colors for each series plotted in the same graph
colors = {
    "strength": "red",
    "dexterity": "blue",
    "constitution": "green",
    "intelligence": "purple",
    "wisdom": "orange",
    "charisma": "magenta",
}
# create the figure. Kind of nice that you can style and title this in the constructor
p = figure(title=config.get("chart_title"), background_fill_color="#fafafa")

# draw all dots - nice that we can feed it a data frame here, too
for stat in config.get("stats"):
    p.scatter(
        x="challenge_rating",
        y=stat,
        color=colors.get(stat, "black"),
        size=10,  # couldn't figure out how to scale sizes to something readable
        source=monster_data,
        legend_label=stat,
    )

# add labels
p.xaxis.axis_label = config.get("x_axis")
p.yaxis.axis_label = config.get("y_axis")
p.add_layout(Label(x=0, y=max(monster_data["strength"]), text=config.get("blurb")))

# show the chart
show(p)

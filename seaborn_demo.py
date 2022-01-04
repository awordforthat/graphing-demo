import seaborn as sns
import matplotlib.pyplot as plt

from util import setup
from config import config

monster_data, challenge_rating, hit_points, armor_class = setup()

# create chart container and graph
fig, ax = plt.subplots()

# draw all dots - no need to extract data column by column!
for stat in config.get("stats"):
    sns.scatterplot(
        x="challenge_rating",
        y=stat,
        size="hit_points",
        sizes=(20, 200),
        label=stat,
        legend=None,
        data=monster_data,
    ).set_title(
        config.get("chart_title")
    )  # chaining the title is nice

# add labels
ax.set_xlabel(config.get("x_axis"))
ax.set_ylabel(config.get("y_axis"))

# add annotation
plt.text(
    0,
    max(monster_data["strength"]),
    config.get("blurb"),
)

# for some reason, the dot sizes are magically better here
plt.legend()

plt.show()  # for some reason, this command is left out of *all* the seaborn docs

import matplotlib
import matplotlib.pyplot as plt

from meta.util import setup
from meta.config import config

monster_data, challenge_rating, hit_points, armor_class = setup()

# set up backend
matplotlib.use("WxAgg")

# if you can't get WxAgg to work, use the following line instead of the one above:
# matplotlib.use("PyQt5")

# create chart container and graph
fig, ax = plt.subplots()

# draw all dots on the scatter plot
for stat in config.get("stats"):
    scatter = ax.scatter(challenge_rating, monster_data[stat], hit_points, label=stat)

# add labels
plt.title(config.get("chart_title"))
plt.xlabel(config.get("x_axis"))
plt.ylabel(config.get("y_axis"))

# add legends
legend = plt.legend()  # auto-detected legend, nice!
# digging into private vars to set legend dot sizes - not so nice
for dot in legend.legendHandles:
    dot._sizes = [30]

matplotlib.pyplot.text(0, max(monster_data["strength"]), config.get("blurb"))

# display the chart
plt.show()

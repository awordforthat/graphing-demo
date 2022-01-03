import matplotlib
import matplotlib.pyplot as plt

from util import load_data
from config import config

matplotlib.use("WxAgg")

monster_data = load_data(["hit_points", "challenge_rating", "armor_class"])

challenge_rating = monster_data["challenge_rating"]
hit_points = monster_data["hit_points"]
armor_class = monster_data["armor_class"]

fig, ax = plt.subplots()

for stat in config.get("stats"):
    scatter = ax.scatter(challenge_rating, monster_data[stat], hit_points, label=stat)

plt.title(config.get("chart_title"))
plt.xlabel(config.get("x_axis"))
plt.ylabel(config.get("y_axis"))

legend = plt.legend()  # auto-detected legend, nice!
# digging into private vars to set legend dot sizes - not so nice
for dot in legend.legendHandles:
    dot._sizes = [30]

matplotlib.pyplot.text(0, max(monster_data["strength"]), config.get("blurb"))

plt.show()

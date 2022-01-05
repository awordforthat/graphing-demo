import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("WxAgg")

normal_sizes = [5, 95]
my_sizes = [0.1, 99.9]


def calc_degrees(pct):
    return 90 - pct / 100 * 360


fig1, axs = plt.subplots(nrows=1, ncols=2)
fig1.set_size_inches(10, 6)
axs[0].pie(normal_sizes, radius=1, startangle=calc_degrees(normal_sizes[0]))
axs[0].set_title("Previous Presentations")
axs[1].pie(my_sizes, radius=1, startangle=calc_degrees(my_sizes[0]))
axs[1].set_title("This Presentation")

plt.suptitle("Percent of Available Content Covered", fontsize=25)
plt.legend(
    loc="lower right", bbox_to_anchor=(1, -0.25), labels=("Covered", "Not covered")
)
plt.show()

# Notes:
# default backend "Agg" is for saving files
# Could not get TkAgg to work (mismatch between tk versions in virtualenv vs matplotlib dependencies?)
# How in the world are legends supposed to be anchored?
# Why does adding a figure title with  override the second subplot title?
# Can you also set the plot size in pixels?

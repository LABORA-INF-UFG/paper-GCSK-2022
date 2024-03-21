import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x_label = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

# Murti
y1 = [24, 30, 53, 146, 86, 187, 238, 258, 381, 380]
agg_murti = [y1[i] + x_label[i] for i in range(0, len(x_label))]
y1 = agg_murti

# DRL
y4 = [23, 54, 101, 148, 268, 180, 289, 348, 398, 428]
agg_drl = [y4[i] + x_label[i] for i in range(0, len(x_label))]
y4 = agg_drl

# PlaceRAN
y3 = [210, 498, 876, 1152, 1441, 1714, -350, -400, -450, -500]
agg_placeran = [y3[i] + x_label[i] for i in range(0, len(x_label))]
y3 = agg_placeran

# y2 = [22, 46, 95, 162, 331, 303, 301]
y2 = [181, 376, 751, 969, 1151, 1330, 841, 1702, 1842, 2104]
agg_GA = [y2[i] + x_label[i] for i in range(0, len(x_label))]
y2 = agg_GA

# The data
# Calculate optimal width
width = np.min(np.diff(x)) / 5

x_label = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

fig = plt.figure(figsize=(10, 3))
ax = fig.add_subplot()
# matplotlib 3.0 you have to use align
ax.bar(x - 2 * width, y1, width, color='lightblue', label='-Ymin', align='edge')
ax.bar(x - width, y4, width, color='slategray', label='Ymax', align='edge')
ax.bar(x, y2, width, color='royalblue', label='Ymax', align='edge')
ax.bar(x + width, y3, width, color='navy', label='Ymax', align='edge')

ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)

plt.rcParams.update({'font.size': 14})
# plt.ylim(0, 1100)

# f, ax = plt.subplots(figsize=(7, 3))

ax.tick_params(axis='y', which='major', labelsize=14)
ax.tick_params(axis='x', which='major', labelsize=14)

plt.xlim(0.4, 10.6)
plt.ylim(0, 3000)

plt.ylabel("Centralized VNFs (#)", fontsize=14)

plt.xlabel('CRs (#)', fontsize=14)

plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_xticklabels(["50", "100", "150", "200", "250", "300", "350", "400", "450", "500"])

legend_elements = [Line2D([0], [0], color='lightblue', lw=3, label='Murti [14]'),
                   Line2D([0], [0], color='slategray', lw=3, label='DRL Agent'),
                   Line2D([0], [0], color='royalblue', lw=3, label='GA'),
                   Line2D([0], [0], color='navy', lw=3, label='PlaceRAN')]
plt.legend(handles=legend_elements, loc="upper left")

plt.savefig("compating_aggregation_all_solutions.pdf", bbox_inches='tight')

plt.show()

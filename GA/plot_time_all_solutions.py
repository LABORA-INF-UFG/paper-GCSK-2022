import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import math

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x_label = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

# Murti
y1 = [0.4, 0.5, 0.9, 1.5, 1.9, 3.1, 4.1, 5.3, 6.4, 8.3]
y1 = [math.log(i) if i > 1 else 0 for i in y1]
# agg_murti = [y1[i] + x_label[i] for i in range(0, len(x_label))]
# y1 = agg_murti

# DRL
y4 = [27, 45, 80, 101, 227, 281, 350, 417, 675, 745]
y4 = [math.log(i) if i > 1 else 0 for i in y4]
# agg_drl = [y4[i] + x_label[i] for i in range(0, len(x_label))]
# y4 = agg_drl

# PlaceRAN
y3 = [114.7, 144.9, 13.3, 1551.4, 43.7, 268.7, -350, -400, -450, -500]
y3 = [math.log(i) if i > 1 else 0 for i in y3]
# agg_placeran = [y3[i] + x_label[i] for i in range(0, len(x_label))]
# y3 = agg_placeran

y2 = [15.7, 25.0, 31.9, 57.7, 82.1, 140.6, 136.6, 118.4, 78.8, 84.6]
y2 = [math.log(i) if i > 1 else 0 for i in y2]
# agg_GA = [y2[i] + x_label[i] for i in range(0, len(x_label))]
# y2 = agg_GA

y10 = [0.15, 0.92, 0.44, 1.55, 1.59, 1.03, 1.9, 0.5, 0.5, 0.6] # [0.15, 0.92, 0.44, 1.55, 1.59, 4.03, 12.9, 0, 0, 0]
y10 = [i if i >= 0 else 0 for i in y10] # math.log(i)

#The data
#Calculate optimal width
width = np.min(np.diff(x))/5

fig = plt.figure(figsize=(10, 3))
ax = fig.add_subplot()
# matplotlib 3.0 you have to use align
ax.bar(x-2*width, y1, width, color='lightblue', label='-Ymin', align='edge')
ax.bar(x-width, y4, width, color='slategray', label='Ymax', align='edge')# , yerr=[0.23, 0.43, 0.3, 0.2, 0.3, 0.4, 0.11, 0.4, 0.70, 0.9])
ax.bar(x, y2, width, color='royalblue', label='Ymax', align='edge')# , yerr=[0.09, 0.15, 0.23, 0.13, 0.14, 0.13, 0.25, 0.15, 0.24, 0.5])
ax.bar(x, y10, width, color='peru', label='Ymax', align='edge', hatch='////')# , yerr=[0.1, 0.2, 0.3, 0.1, 0.1, 0.2, 0.15, 0.2, 0.1, 0.3])
ax.bar(x+width, y3, width, color='navy', label='Ymax', align='edge')

ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)


plt.rcParams.update({'font.size': 11})
plt.ylim(0, 10)

# f, ax = plt.subplots(figsize=(7, 3))

ax.tick_params(axis='y', which='major', labelsize=14)
ax.tick_params(axis='x', which='major', labelsize=14)

# plt.xlim(0.4, 2.6)

plt.ylabel("Time (ms)", fontsize=14)

plt.xlabel('CRs (RUs)', fontsize=14)
plt.yticks([2, 4, 6, 8, 10])
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_xticklabels(["50", "100", "150", "200", "250", "300", "350", "400", "450", "500"])

legend_elements = [Line2D([0], [0], color='darkgray', lw=3, label='Murti [14]'),
                   Line2D([0], [0], color='slategray', lw=3, label='DRL Agent'),
                   Line2D([0], [0], color='royalblue', lw=3, label='GA'),
                   Line2D([0], [0], color='navy', lw=3, label='PlaceRAN')]
plt.legend(handles=legend_elements, loc="upper left")

plt.savefig("comparing_solutions_time.pdf", bbox_inches='tight')

plt.show()

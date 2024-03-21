import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_Murti = [i*1000 for i in [0.16,  0.34, 0.63, 0.96, 1.29, 1.71, 2.3, 2.7, 3.2, 4.0]]
y_DRL = [i*1000 for i in [96, 262, 504, 709, 1159, 1655, 2151, 2758, 3583, 4268]]
y_PlaceRAN = [i*1000 for i in [0.34, 0.92, 1.88, 3.19, 4.57, 6.98, 8.69, 12.06, 13.88, 17.78]]
y_GA = [i*1000 for i in [13.8, 31.5, 50.3, 68.0, 91.3, 115.4, 141.8, 168.4, 194.9, 221.3]]
GA_sol_1 = [i*1000 for i in [0.01, 0.04, 0.07, 0.09, 0.12, 0.15, 0.19, 0.47, 0.29, 0.32]]
GA_best_sol = [i*1000 for i in [13, 29, 45, 0.09, 0.11, 0.15, 0.19, 166, 0.28, 0.43]]

fig = plt.figure(figsize=(10, 3))

m_size = 10
lw_size = 3
plt.plot(x, y_Murti, color="firebrick", marker="o", markersize=m_size, lw=lw_size)
plt.plot(x, y_DRL, color="gray", marker="v", markersize=m_size, lw=lw_size)
plt.plot(x, y_PlaceRAN, color="navy", marker="o", markersize=m_size, lw=lw_size)
plt.plot(x, y_GA, color="royalblue", marker="^", markersize=m_size, lw=lw_size)
plt.plot(x, GA_sol_1, color="peru", marker="^", linestyle='--', markersize=m_size, lw=lw_size)
# plt.plot(x, GA_best_sol, color="darkgreen", marker="^", linestyle='--', markersize=m_size, lw=lw_size)
plt.yscale("log")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xticks(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], labels=["50", "100", "150", "200", "250", "300", "350", "400", "450", "500"], fontsize=20)
plt.yticks(ticks=[10**0, 10**2, 10**4, 10**6, 10**8], fontsize=20)

plt.ylabel("Time (ms)", fontsize=20)
plt.xlabel('RUs (#)', fontsize=20)

# plt.rcParams.update({'font.size': 20})
#
# legend_elements = [Line2D([0], [0], color='firebrick', lw=3, label='Murti [14]'),
#                    Line2D([0], [0], color='navy', lw=3, label='PlaceRAN'),
#                    Line2D([0], [0], color='royalblue', lw=3, label='GA'),
#                    Line2D([0], [0], color='peru', lw=3, label='GA 1#')]
# plt.legend(handles=legend_elements, loc="upper left", ncol=4)

plt.savefig("line_time.pdf", bbox_inches='tight')

plt.show()

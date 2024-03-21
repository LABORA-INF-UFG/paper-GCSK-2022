import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_PlaceRAN = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x_DRL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y_DRL = [i*1000 for i in [215, 692, 1374, 2275, 3604, 4809, 6502, 8844, 10540, 13000]]
y_PlaceRAN = [i*1000 for i in [1.72, 14.4, 15.2, 148.43, 234.8, 1129.39, 2863.0, 5428.10, 86000]] #, 6.98, 8.69, 12.06, 13.88, 17.78]]
y_GA = [i*1000 for i in [14.7, 32.8, 52.4, 73.2, 95.1, 119.8, 146.0, 173.1, 201.98, 262.9]]
GA_sol_1 = [i*1000 for i in [0.02, 0.06, 0.11, 0.17, 0.33, 0.29, 0.45, 0.52, 0.87, 1.25]]
GA_best_sol = [i*1000 for i in [0.02, 0.06, 0.12, 0.17, 0.33, 0.33, 0.51, 0.70, 0.77, 1.05]]

fig = plt.figure(figsize=(10, 3))

m_size = 10
lw_size = 3

plt.plot(x, y_DRL, color="gray", marker="v", markersize=m_size, lw=lw_size)
plt.plot(x_PlaceRAN, y_PlaceRAN, color="navy", marker="o", markersize=m_size, lw=lw_size)
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
#                    Line2D([0], [0], color='royalblue', lw=3, label='GA complete search'),
#                    Line2D([0], [0], color='peru', lw=3, label='GA first solution'),
#                    Line2D([0], [0], color='darkgreen', lw=3, label='GA best solution')]
# plt.legend(handles=legend_elements, loc="upper left")

plt.savefig("line_time_k4.pdf", bbox_inches='tight')

plt.show()

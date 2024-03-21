import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y_constant = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

y_Murti = [-34, -68, -46, -66, -100, -99, -147, -209, -201, -242]
y_DRL = [92, 88, 175, 44, 490, 354, 403, 547, 706, 524]
GA_sol_1 = [105, 162, 259, 263, 485, 590, 646, 480, 790, 883]
y_GA = [117, 182, 297, 263, 485, 590, 646, 627, 812, 883]
y_PlaceRAN = [117, 188, 322, 283, 556, 673, 752, 869, 945, 1025]

for i in range(0, len(y_constant)):
    y_Murti[i] += y_constant[i]
    y_DRL[i] += y_constant[i]
    y_GA[i] += y_constant[i]
    GA_sol_1[i] += y_constant[i]
    y_PlaceRAN[i] += y_constant[i]

fig = plt.figure(figsize=(10, 3))
m_size = 10
lw_size = 3
plt.plot(x, y_Murti, color="firebrick", marker="o", markersize=m_size, lw=lw_size)
plt.plot(x, y_DRL, color="gray", marker="v", markersize=m_size, lw=lw_size)
plt.plot(x, GA_sol_1, color="peru", marker="^", linestyle='--', markersize=m_size, lw=lw_size)
plt.plot(x, y_PlaceRAN, color="navy", marker="o", markersize=m_size, lw=lw_size)
plt.plot(x, y_GA, color="royalblue", marker="^", markersize=m_size, lw=lw_size)
# plt.yscale("log")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xticks(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], labels=["50", "100", "150", "200", "250", "300", "350", "400", "450", "500"], fontsize=20)
plt.yticks(ticks=[0, 200, 400, 600, 800, 1000, 1200, 1400, 1600], fontsize=18)

plt.ylabel("Centralization (#)", fontsize=18)
plt.xlabel('RUs (#)', fontsize=20)

plt.savefig("line_agg_handmade.pdf", bbox_inches='tight')

plt.show()

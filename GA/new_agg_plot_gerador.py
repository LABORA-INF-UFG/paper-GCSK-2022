import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_PlaceRAN = [1, 2, 3, 4, 5, 6]

y_constant = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

y_Murti = [24, 30, 53, 146, 86, 187, 238, 258, 381, 380]
y_DRL = [23, 54, 101, 148, 268, 180, 289, 348, 398, 428]
y_GA = [181, 376, 751, 969, 1151, 1330, 841, 1702, 1842, 2104]
y_PlaceRAN = [210, 498, 876, 1152, 1441, 1714]
GA_sol_1 = [89, 205, 477, 634, 746, 864, -197, 1195, 1315, 1592]

for i in range(0, len(y_constant)):
    y_Murti[i] += y_constant[i]
    y_DRL[i] += y_constant[i]
    y_GA[i] += y_constant[i]
    GA_sol_1[i] += y_constant[i]
    if i < 6:
        y_PlaceRAN[i] += y_constant[i]

fig = plt.figure(figsize=(10, 3))
m_size = 7
plt.plot(x, y_Murti, color="firebrick", marker="o", markersize=m_size)
plt.plot(x, y_DRL, color="gray", marker="s", markersize=m_size)
plt.plot(x, y_GA, color="royalblue", marker="s", markersize=m_size)
plt.plot(x_PlaceRAN, y_PlaceRAN, color="navy", marker="o", markersize=m_size)
plt.plot(x, GA_sol_1, color="peru", marker="s", linestyle='--', markersize=m_size)
plt.yscale("log")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xticks(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], labels=["50", "100", "150", "200", "250", "300", "350", "400", "450", "500"], fontsize=14)
plt.yticks(ticks=[10**0, 10**1, 10**2, 10**3, 10**4], fontsize=14)

plt.ylabel("Centralization level (#)", fontsize=14)
plt.xlabel('CRs (#)', fontsize=14)

plt.savefig("line_agg_generator.pdf", bbox_inches='tight')

plt.show()

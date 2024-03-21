import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_PlaceRAN = [1, 2, 3, 4, 5, 6]

y_Murti = [i*1000 for i in [0.4, 0.5, 0.9, 1.5, 1.9, 3.1, 4.1, 5.3, 6.4, 8.3]]
y_DRL = [i*1000 for i in [27, 45, 80, 101, 227, 281, 350, 417, 675, 745]]
y_GA = [i*1000 for i in [15.7, 25.0, 31.9, 57.7, 82.1, 140.6, 136.6, 118.4, 78.8, 84.6]]
y_PlaceRAN = [i*1000 for i in [114.7, 144.9, 13.3, 1551.4, 43.7, 268.7]]
GA_sol_1 = [i*1000 for i in [0.15, 0.92, 0.44, 1.55, 1.59, 1.03, 1.9, 0.5, 0.5, 0.6]]

fig = plt.figure(figsize=(10, 3))
m_size = 7
plt.plot(x, y_Murti, color="firebrick", marker="o", markersize=m_size)
plt.plot(x, y_DRL, color="gray", marker="s", markersize=m_size)
plt.plot(x, y_GA, color="royalblue", marker="s", markersize=m_size)
plt.plot(x_PlaceRAN, y_PlaceRAN, color="navy", marker="o", markersize=m_size)
plt.plot(x, GA_sol_1, color="peru", marker="s", markersize=m_size)
plt.yscale("log")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xticks(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], labels=["50", "100", "150", "200", "250", "300", "350", "400", "450", "500"], fontsize=14)
plt.yticks(ticks=[10**0, 10**2, 10**4, 10**6, 10**8], fontsize=14)

plt.ylabel("Time (ms)", fontsize=14)
plt.xlabel('CRs (#)', fontsize=14)

plt.savefig("line_time_gerador.pdf", bbox_inches='tight')

plt.show()

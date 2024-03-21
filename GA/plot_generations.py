import json
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

q_CRs = 500

plt.rcParams["figure.figsize"] = (10, 4)
plt.rcParams.update({'font.size': 14})

for test in range(1, 31):
    file = open("Topology_T2_{}_CRs_result/fistness_history_test_{}.json".format(q_CRs, test))
    json_obj = json.load(file)
    best_cromo_history = json_obj["history"]
    best_cromo_history = [i * (-1) for i in best_cromo_history]
    plt.plot(best_cromo_history)

optimal_value = {8: 22, 16: 46, 32: 95, 64: 165, 128: 399, 256: 436, 500: 796}

optimal = [optimal_value[q_CRs] for i in range(0, len(best_cromo_history))]

plt.plot(optimal, color='r', linestyle='--', lw=1.3)
plt.ylabel('Fitness (#)', fontsize=15)
plt.xlabel('Generation', fontsize=15)
plt.grid(linestyle="--")
plt.title("Best chromosome fitness - {} CRs".format(q_CRs), fontsize=15)

legend_elements = [Line2D([0], [0], color='black', lw=2, label='Test'),
                   Line2D([0], [0], color='r', lw=2, linestyle="--", label='Optimal')]
plt.legend(handles=legend_elements, loc="lower right")

plt.savefig("Topology_T2_{}_CRs_result/best_cromo_history.pdf".format(q_CRs), bbox_inches="tight")

plt.show()
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.rcParams.update({'font.size': 20})

legend_elements = [Line2D([0], [0], color='firebrick', lw=3, label='Murti [11]', marker='o', markersize=10),
                   Line2D([0], [0], color='gray', lw=3, label='DRL Agent [12]', marker='v', markersize=10),
                   Line2D([0], [0], color='peru', lw=3, label='GA 1ˢᵗ solution', marker='^', markersize=10),
                   Line2D([0], [0], color='royalblue', lw=3, label='GA best solution', marker='^', markersize=10),
                   Line2D([0], [0], color='navy', lw=3, label='PlaceRAN [4]', marker='o', markersize=10)]
plt.legend(handles=legend_elements, loc="upper left")

plt.savefig("legend.pdf", bbox_inches='tight')

plt.show()

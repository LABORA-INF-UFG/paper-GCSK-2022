import os

for topo in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
    os.system("rm -rf Topology_T2_{}_CRs_result/*".format(topo))
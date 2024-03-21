import os

for q_CRs in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
    os.system("cp {}_CRs/New_T2_{}_CRs.json /home/gmfaria6/workspace/DRL/DRL-MPP-RAN/topology/murti_files/murti_{}_CRs_nodes.json".format(q_CRs, q_CRs, q_CRs))
    os.system("cp {}_CRs/New_T2_{}_links.json /home/gmfaria6/workspace/DRL/DRL-MPP-RAN/topology/murti_files/murti_{}_CRs_links.json".format(q_CRs, q_CRs, q_CRs))
    os.system("cp {}_CRs/Murti_T2_{}_paths.json /home/gmfaria6/workspace/DRL/DRL-MPP-RAN/topology/murti_files/{}_CRs_paths.json".format(q_CRs, q_CRs, q_CRs))


print("DONE")

import json
import random
import networkx as nx
import matplotlib.pyplot as plt
import os
# import scipy as sp

plt.rcParams["figure.figsize"] = (10, 4)
plt.rcParams.update({'font.size': 14})

q_CRs = 450

layer_order = [q_CRs*4/100, q_CRs*16/100, q_CRs*70/100, q_CRs*10/100]

CRs_ID_per_layer = {1: [], 2: [], 3: [], 4: []}

nodes = []
links = []
node_id = 1
links_tuple = []

for i in range(0, q_CRs):
    if node_id < layer_order[0] + 1:
        nodes.append({"nodeNumber": node_id, "cpu": random.choice([128, 64]), "RU": 0})
        cap = random.choice([q_CRs * 20, q_CRs * 10])
        lat = random.choice([0.161, 0.174, 0.22])
        links.append({"fromNode": 0, "toNode": node_id, "delay": lat, "capacity": cap})
        links.append({"fromNode": node_id, "toNode": 0, "delay": lat, "capacity": cap})
        links_tuple.append((0, node_id))
        CRs_ID_per_layer[1].append(node_id)

    elif node_id < layer_order[0]+layer_order[1] + 1:
        nodes.append({"nodeNumber": node_id, "cpu": random.choice([64, 32]), "RU": 1})
        new_links = []
        for j in range(0, 4): # ALTERAR PARA 3 CASO TENHAM MAIS LINKS NO HL1
            f = True
            while f:
                new_l = random.choice(CRs_ID_per_layer[1])
                if new_l not in new_links:
                    new_links.append(new_l)
                    cap = random.choice([q_CRs * 8, q_CRs * 5])
                    lat = random.choice([0.174, 0.22, 0.29])
                    links.append({"fromNode": new_l, "toNode": node_id, "delay": lat, "capacity": cap})
                    links.append({"fromNode": node_id, "toNode": new_l, "delay": lat, "capacity": cap})
                    links_tuple.append((new_l, node_id))
                    f = False

        CRs_ID_per_layer[2].append(node_id)

    elif node_id < layer_order[0]+layer_order[1]+layer_order[2] + 1:
        nodes.append({"nodeNumber": node_id, "cpu": random.choice([32, 16]), "RU": 1})
        new_links = []
        for j in range(0, 6):
            f = True
            while f:
                new_l = random.choice(CRs_ID_per_layer[2])
                if new_l not in new_links:
                    new_links.append(new_l)
                    cap = random.choice([q_CRs * 5, q_CRs * 4])
                    lat = random.choice([0.29, 0.354, 0.44])
                    links.append({"fromNode": new_l, "toNode": node_id, "delay": lat, "capacity": cap})
                    links.append({"fromNode": node_id, "toNode": new_l, "delay": lat, "capacity": cap})
                    links_tuple.append((new_l, node_id))
                    f = False

        CRs_ID_per_layer[3].append(node_id)

    elif node_id < layer_order[0]+layer_order[1]+layer_order[2]+layer_order[3] + 1:
        nodes.append({"nodeNumber": node_id, "cpu": random.choice([16, 8]), "RU": 1})
        new_links = []
        for j in range(0, 6):
            f = True
            while f:
                new_l = random.choice(CRs_ID_per_layer[3])
                if new_l not in new_links:
                    new_links.append(new_l)
                    cap = random.choice([q_CRs * 3, q_CRs * 2])
                    lat = random.choice([0.169, 0.22, 0.44, 0.501])
                    links.append({"fromNode": new_l, "toNode": node_id, "delay": lat, "capacity": cap})
                    links.append({"fromNode": node_id, "toNode": new_l, "delay": lat, "capacity": cap})
                    links_tuple.append((new_l, node_id))
                    f = False

        CRs_ID_per_layer[4].append(node_id)

    node_id += 1

G = nx.Graph()
G.add_edges_from(links_tuple)
nx.draw(G, node_size=50, arrowsize=2)
plt.show()
os.system("pwd")
json.dump({"nodes": nodes}, open("/home/gmfaria6/workspace/ICC_2022_GA_Placement_Problem/PlaceRAN/model_files/topology_files/{}_CRs/New_T2_{}_CRs.json".format(q_CRs, q_CRs), 'w'))
json.dump({"links": links}, open("/home/gmfaria6/workspace/ICC_2022_GA_Placement_Problem/PlaceRAN/model_files/topology_files/{}_CRs/New_T2_{}_links.json".format(q_CRs, q_CRs), 'w'))
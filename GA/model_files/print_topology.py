import json
import networkx as nx
import matplotlib.pyplot as plt

q_CRs = 8

topology_obj = json.load(open("model_files/topology_files/{}_CRs/T2_{}_CRs.json".format(q_CRs, q_CRs), 'r'))
nodes = topology_obj["nodes"]

topology_obj = json.load(open("model_files/topology_files/{}_CRs/T2_{}_links.json".format(q_CRs, q_CRs), 'r'))
links = topology_obj["links"]

nodes_ID_list = []
DUs_node_ID_list = []
links_tuple_list = []

for node in nodes:
    nodes_ID_list.append(node["ID"])

for DU in DUs:
    DUs_node_ID_list.append(DU["node"])

for link in links:
    links_tuple_list.append((link["from_Node"], link["to_Node"]))

nodes_without_DU = []

for n in nodes_ID_list:
    if n not in DUs_node_ID_list and n not in [0, 1]:
        nodes_without_DU.append(n)

G = nx.Graph()

G.add_nodes_from(nodes_ID_list)
G.add_edges_from(links_tuple_list)
pos = nx.spring_layout(G)
print(DUs_node_ID_list)

nx.draw_networkx_nodes(G, pos, nodelist=nodes_without_DU, node_color='royalblue', node_shape='s')
nx.draw_networkx_nodes(G, pos, nodelist=DUs_node_ID_list, node_color='orangered', node_shape='^')
nx.draw_networkx_nodes(G, pos, nodelist=[1], node_color='red', node_shape='o', label="CU")
nx.draw_networkx_nodes(G, pos, nodelist=[0], node_color='navy', node_shape='o')
nx.draw_networkx_edges(G, pos, links_tuple_list)

# shift position a little bit
shift = [0.05, 0]
shifted_pos ={node: node_pos + shift for node, node_pos in pos.items()}

# Just some text to print in addition to node ids
labels = {}
for du in DUs_node_ID_list:
    labels[du] = "DU"
labels[0] = "Core"
labels[1] = "CU"
nx.draw_networkx_labels(G, shifted_pos, labels=labels, horizontalalignment="left")

plt.savefig("topology.pdf")
plt.show()
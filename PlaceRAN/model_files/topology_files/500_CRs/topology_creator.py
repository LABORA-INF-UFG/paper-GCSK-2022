import json
import random

len_new_topo = 700

CRs_obj = json.load(open("T2_500_CRs.json", 'r'))
links_obj = json.load(open("T2_500_links.json", 'r'))

CRs_list = CRs_obj["nodes"]
links_list = links_obj["links"]

crs = []

for cr in CRs_list:
    crs.append(cr["nodeNumber"])

selected_CRs = []
new_CRs_relation = {}
new_CRs_list = CRs_list.copy()

for i in range(500, len_new_topo):
    selected_CR = random.choice(crs)
    selected_CRs.append(selected_CR)
    new_ID = random.randrange(1, 999999)
    while new_ID not in crs:
        new_ID = random.randrange(1, 999999)
    new_CRs_relation[selected_CR] = new_ID
    new_CRs_list.append({'nodeNumber': new_ID, 'cpu': 16, 'RU': 1})

print(selected_CR)
print(new_CRs_relation)

new_link_list = links_list.copy()

for l in links_list:
    if l["fromNode"] in new_CRs_relation.keys():
        new_link_list.remove(l)
        new_link_list.append({'fromNode': l["fromNode"], 'toNode': new_CRs_relation[l["fromNode"]], 'delay': l["delay"], 'capacity': l["capacity"]})
        new_link_list.append({'fromNode': new_CRs_relation[l["fromNode"]], 'toNode': l["toNode"], 'delay': l["delay"], 'capacity': l["capacity"]})

print(new_link_list)
json.dump({"links": new_link_list}, open("../{}_CRs/T2_{}_links.json".format(len_new_topo, len_new_topo), 'w'))
json.dump({"nodes": new_CRs_list}, open("../{}_CRs/T2_{}_CRs.json".format(len_new_topo, len_new_topo), 'w'))

import json
import random
import os

paths = []
k = 0
k_stop = 4

q_CRs = 450

layer_order = [q_CRs*4/100, q_CRs*16/100, q_CRs*70/100, q_CRs*10/100]

os.system("pwd")
link_file = open("/home/gmfaria6/workspace/ICC_2022_GA_Placement_Problem/PlaceRAN/model_files/topology_files/{}_CRs/New_T2_{}_links.json".format(q_CRs, q_CRs))
json_obj = json.load(link_file)
links = json_obj["links"]

adjacencia = {}

paths = []

for i in range(0, q_CRs+1):
    adjacencia[i] = []
    for l in links:
        if l["toNode"] == i and l["fromNode"] < l["toNode"]:
            adjacencia[i].append(l["fromNode"])

count = 1

for i in range(0, q_CRs+1):
    if i <= layer_order[0]:
        pass
    elif i <= layer_order[0] + layer_order[1]:
        cr_list = random.sample(adjacencia[i], k_stop)
        for cr in cr_list:
            paths.append([0, cr, i])
    elif i <= layer_order[0] + layer_order[1] + layer_order[2]:
        cr_list = random.sample(adjacencia[i], k_stop)
        for cr in cr_list:
            tmp_cr = random.choice(adjacencia[cr])
            paths.append([0, tmp_cr, cr, i])
    elif i <= layer_order[0] + layer_order[1] + layer_order[2] + layer_order[3]:
        cr_list = random.sample(adjacencia[i], k_stop)
        for cr in cr_list:
            tmp_cr1 = random.choice(adjacencia[cr])
            tmp_cr2 = random.choice(adjacencia[tmp_cr1])
            paths.append([0, tmp_cr2, tmp_cr1, cr, i])

print(paths)

with open('/home/gmfaria6/workspace/ICC_2022_GA_Placement_Problem/PlaceRAN/model_files/topology_files/{}_CRs/Murti_T2_{}_paths.json'.format(q_CRs, q_CRs), 'w') as json_file:
    data = {}
    data["paths"] = {}
    path_data = {}
    seq = []
    count = 2
    id = 1
    for path in paths:
        for position in range(0, len(path) - 1):
            if position == count:
                seq.append(path[1])
                p1 = []
                edge = "({}, {})".format(str(path[0]), str(path[1]))
                p1.append(edge)
                seq.append(path[position])
                p2 = []
                for i in range(1, len(path) - 1):
                    if i != position:
                        edge = "({}, {})".format(str(path[i]), str(path[i + 1]))
                        p2.append(edge)
                    if i + 1 == position:
                        break
                seq.append(path[len(path) - 1])
                p3 = []
                for i in range(position, len(path) - 1):
                    if i != len(path) - 1:
                        edge = "({}, {})".format(str(path[i]), str(path[i + 1]))
                        p3.append(edge)
                    if i + 1 == position:
                        break
                count += 1
                p = {}
                p["id"] = id
                p["source"] = "CN"
                p["target"] = path[len(path) - 1]
                p["seq"] = seq
                p["p1"] = p1
                p["p2"] = p2
                p["p3"] = p3
                append = True
                if path_data:
                    for i in path_data:
                        p_i = path_data[i]
                        if p_i:
                            if p_i["p1"] == p["p1"] and p_i["p2"] == p["p2"] and p_i["p3"] == p["p3"] and p_i[
                                "id"] != \
                                    p["id"]:
                                append = False
                if append:
                    path_data["path-{}".format(str(id))] = p
                    id += 1
            seq = []
        count = 2
    count = 1
    for path in paths:
        for position in range(0, len(path) - 1):
            if position == count:
                seq.append(path[0])
                p1 = []
                seq.append(path[position])
                p2 = []
                for i in range(0, len(path) - 1):
                    if i != position:
                        edge = "({}, {})".format(str(path[i]), str(path[i + 1]))
                        p2.append(edge)
                    if i + 1 == position:
                        break
                seq.append(path[len(path) - 1])
                p3 = []
                for i in range(position, len(path) - 1):
                    if i != len(path) - 1:
                        edge = "({}, {})".format(str(path[i]), str(path[i + 1]))
                        p3.append(edge)
                    if i + 1 == position:
                        break
                count += 1
                p = {}
                p["id"] = id
                p["source"] = "CN"
                p["target"] = path[len(path) - 1]
                p["seq"] = seq
                p["p1"] = p1
                p["p2"] = p2
                p["p3"] = p3
                append = True
                if path_data:
                    for i in path_data:
                        p_i = path_data[i]
                        if p_i:
                            if p_i["p1"] == p["p1"] and p_i["p2"] == p["p2"] and p_i["p3"] == p["p3"]:
                                append = False
                if append:
                    path_data["path-{}".format(str(id))] = p
                    id += 1
            seq = []
        count = 1
    for path in paths:
        seq.append(0)
        p1 = []
        seq.append(0)
        p2 = []
        seq.append(path[len(path) - 1])
        p3 = []
        for i in range(0, len(path) - 1):
            if i != len(path) - 1:
                edge = "({}, {})".format(str(path[i]), str(path[i + 1]))
                p3.append(edge)
            if i + 1 == (len(path) - 1):
                break
        p = {}
        p["id"] = id
        p["source"] = "CN"
        p["target"] = path[len(path) - 1]
        p["seq"] = seq
        p["p1"] = p1
        p["p2"] = p2
        p["p3"] = p3
        p["p3"] = p3
        p["p3"] = p3
        append = True
        if path_data:
            for i in path_data:
                p_i = path_data[i]
                if p_i:
                    if p_i["p1"] == p["p1"] and p_i["p2"] == p["p2"] and p_i["p3"] == p["p3"] and p_i["id"] != p[
                        "id"]:
                        append = False
        if append:
            path_data["path-{}".format(str(id))] = p
            id += 1
        seq = []
    data["paths"] = path_data
    sum = 0
    for iten in path_data:
        sum += 1
    print("{} paths configurations successfully found".format(sum))
    json.dump(data, json_file, indent=4)

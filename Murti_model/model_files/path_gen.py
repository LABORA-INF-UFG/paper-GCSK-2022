import json
import networkx as nx
import random

paths = []
k = 0
k_stop = 1
q_CRs = 100


with open('model_files/topology_files/{}_CRs/New_T2_{}_links.json'.format(q_CRs, q_CRs)) as json_file:
    data = json.load(json_file)
    json_links = data["links"]
    links = []
    for l in json_links:
        links.append((l["fromNode"], l["toNode"]))
    dst = []
    with open('model_files/topology_files/{}_CRs/New_T2_{}_CRs.json'.format(q_CRs, q_CRs)) as dst_file:
        json_dst = json.load(dst_file)
        nodes = json_dst["nodes"]
        for item in nodes:
            if item["RU"]:
                dst.append(item["nodeNumber"])
    G = nx.Graph()
    G.add_edges_from(links)
    dus_relation = []
    dus_count_list = {}
    for cr in nodes:
        if cr["RU"] == 1:
            destination_node = cr["nodeNumber"]
            s_path = nx.shortest_path(G, source=0, target=destination_node)
            paths.append(s_path)
            du = 0
            while du == 0:
                # print("Calculating DU for RU {}".format(cr["nodeNumber"]))
                tmp_du = random.choice(s_path)
                if s_path[len(s_path) - 1] == 5555 or tmp_du == 0:
                    du = 0
                    break
                elif tmp_du != s_path[len(s_path) - 1]: # and random.randrange(0, 5) > 3:
                    if tmp_du not in dus_count_list:
                        dus_count_list[tmp_du] = 1
                        du = tmp_du
                    elif dus_count_list[tmp_du] < 1:
                        dus_count_list[tmp_du] += 1
                        du = tmp_du
            # print(dus_count_list)
            ru = s_path[len(s_path) - 1]
            dus_relation.append({"RU": ru, "DU": du})

            # for l in json_links:
            #     dus_relation.append({"RU": l["toNode"], "DU": l["fromNode"]})
            #         # l["delay"] = 0.001
            #         # l["capacity"] = 2000
            for cr in nodes:
                if cr["nodeNumber"] <= q_CRs*4/100:
                    cr["RU"] = 0
                elif cr["nodeNumber"] == du:
                    cr["RU"] = 1
    new_links = open('model_files/topology_files/{}_CRs/Murti_T2_{}_links.json'.format(q_CRs, q_CRs), 'w')
    json.dump(data, new_links)

    new_nodes = open('model_files/topology_files/{}_CRs/Murti_T2_{}_CRs.json'.format(q_CRs, q_CRs), 'w')
    json.dump(json_dst, new_nodes)

# print(paths)

with open('model_files/topology_files/{}_CRs/Murti_T2_{}_paths.json'.format(q_CRs, q_CRs), 'w') as json_file:
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
                            if p_i["p1"] == p["p1"] and p_i["p2"] == p["p2"] and p_i["p3"] == p["p3"] and p_i["id"] != \
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
                    if p_i["p1"] == p["p1"] and p_i["p2"] == p["p2"] and p_i["p3"] == p["p3"] and p_i["id"] != p["id"]:
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

    dus_file = open('model_files/topology_files/{}_CRs/Murti_T2_{}_DUs.json'.format(q_CRs, q_CRs), 'w')
    json.dump({"DUs": dus_relation}, dus_file)
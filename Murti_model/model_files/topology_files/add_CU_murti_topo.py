import json

files = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

for i in files:
    json_obj = json.load(open("{}_CRs/T2_{}_CRs.json".format(i, i)))
    CRs = json_obj["nodes"]
    CRs.append({'nodeNumber': 5555, 'cpu': 256, 'RU': 0})
    json.dump({"nodes": CRs}, open("{}_CRs/T2_{}_CRs.json".format(i, i), 'w'))



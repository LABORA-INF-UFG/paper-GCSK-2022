import json
q_CRs = 150
json_obj = json.load(open("{}_CRs/Murti_T2_{}_DUs.json".format(q_CRs, q_CRs), 'r'))

dus = {}

for i in json_obj["DUs"]:
    if i["DU"] not in dus:
        dus[i["DU"]] = 1
    else:
        dus[i["DU"]] += 1

print(dus)
import json
import statistics

for q_CRs in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
    maior = 0
    time_f = 999999
    id_test = 0
    first_sol = 0
    for test in range(1, 6):
        json_obj = json.load(open("Topology_T2_{}_CRs_result/fistness_history_test_{}.json".format(q_CRs, test)))
        history = json_obj["history"]
        if history[0] * (-1) > first_sol:
            first_sol = history[0]
        if history[len(history)-1] * (-1) > maior:
            maior = history[len(history)-1] * (-1)

    find_time = []
    all_times = []
    for test in range(1, 6):
        agg_obj = json.load(open("Topology_T2_{}_CRs_result/fistness_history_test_{}.json".format(q_CRs, test)))
        time_obj = json.load(open("Topology_T2_{}_CRs_result/history_time_{}.json".format(q_CRs, test)))
        time_list = time_obj["time"]
        agg_list = agg_obj["history"]
        all_times.append(time_list[len(time_list)-1])
        for i in range(0, len(agg_list)):
            if agg_list[i]*(-1) == maior:
                find_time.append(time_list[i])
                break
    print("{} CRs: Best Solution: {} - with {}s\t\tfirst_solution: FO {}, {}s".format(q_CRs, maior, find_time[0], first_sol, time_list[0]))
    print(statistics.mean(all_times))

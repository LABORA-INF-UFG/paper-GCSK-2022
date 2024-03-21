from collections import OrderedDict

solution = "0258561901671446145937676756364904163626272566216660380438786716111121266678361105126669012427014602043701122032387724781156360514112998390516495757276749665998"

VNCs_list = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 0: 0}

for count in range(0, len(solution)):
    if count % 2 != 0:
        VNCs_list[int(solution[count])] += 1

for vnc in VNCs_list:
    print("VNC {} = {}".format(vnc, VNCs_list[vnc]))
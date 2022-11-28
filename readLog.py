
logFile = open("populate.log", 'r', newline='')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

if __name__ == "__main__":
    pa = 0
    pb = 0
    pc = 0
    pd = 0
    ab = 0
    bc = 0
    cd = 0
    da = 0
    num_of_cycles = []

    with open("populate.log", 'r') as f:
        for line in f:
            word = line.rstrip("\n").split(" ")
            print(word[0:len(word)])
            if word[14] == word[20]:
                if word[14] == 'A':
                    pa += 1
                if word[14] == 'B':
                    pb += 1
                if word[14] == 'C':
                    pc += 1
                if word[14] == 'D':
                    pd += 1
            if "A" in word and "B" in word:
                ab += 1
            if "A" in word and "D" in word:
                da += 1
            if "B" in word and "C" in word:
                bc += 1
            if "C" in word and "D" in word:
                cd += 1
    with open("populate.log", 'r') as f:
        line = f.readlines()
        packet_num = []
        cycle_num = []
        first = []
        last = []
        print(line)
        for i in range(len(line)):
            packet_num.append(int(line[i].rstrip("\n").split(" ")[-1]))
            cycle_num.append(int(line[i].rstrip("\n").split(" ")[0]))

        for i in range(max(packet_num)):
            # first occurence index of packet (i+1) is stored in first (corresponding cycle num is stored in first)
            first.append(cycle_num[packet_num.index(i+1)])
        packet_num.reverse()
        cycle_num.reverse()
        for i in range(max(packet_num)):
            last.append(cycle_num[packet_num.index(i+1)])

        for i in range(max(packet_num)):
            num_of_cycles.append(last[i] - first[i] + 1)


    packet_id = list(range(1, len(num_of_cycles)+1, 1))
    plt2.plot(packet_id, num_of_cycles, '-ok')

    data = {'A_PE': pa, 'B_PE': pb, 'C_PE': pc, 'D_PE': pd, 'A-B': ab, 'B-C': bc, 'C-D': cd, 'D-A': da}
    links = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(links, values, color='maroon',
            width=0.4)

    plt.xlabel("Router Links")
    plt.ylabel("Frequency of various links used for flit transfer")
    plt.title("Link Frequency")
    plt.show()





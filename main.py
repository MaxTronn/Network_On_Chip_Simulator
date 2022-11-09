# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import noc

if __name__ == '__main__':
    with open('traffic.txt', 'r') as file:
        packetList = []
        cycleList = []
        line = file.readlines()
        decto2bin = ['00', '01', '10', '11']
        for i in range(len(line)):
            min_ind = i
            cyclei = int(line[min_ind].split(" ")[0])
            for j in range(i+1, len(line)):
                cyclej = int(line[j].split(" ")[0])
                if cyclei > cyclej:
                    min_ind = j

            line[i], line[min_ind] = line[min_ind], line[i]

        for i in range(1):
            bitword = line[i].split(" ")

            cycle = int(bitword[0])
            src = decto2bin[int(bitword[1])]
            dest = decto2bin[int(bitword[2])]
            loadbits = bitword[3]
            header = "00" + src + dest + bin(random.getrandbits(28)).replace("0b", "")
            payload = []
            for j in range(3):
                payload.append("01" + loadbits[j * 32:(j + 1) * 32])
            tail = "11" + bin(random.getrandbits(32)).replace("0b", "")
            cycleList.append(cycle)
            packet = [header, payload[0], payload[1], payload[2], tail]
            packetList.append(packet)

            print(header + " " + payload[0] + " " + payload[1] + " " + payload[2] + " " + tail+"\n")

    # noc_obj = noc.Noc('XY', packetList, cycleList)
    # noc_obj.mesh_connect()
    # print(noc_obj.router_list[1][0].east.connected_router_port.owner_router.name)
    # print(noc_obj.router_list[1][0].east.connected_router_port.name)

    noc_obj = noc.Noc('YX' , cycleList, packetList)
    noc_obj.start_communication()

    # print(type(packetList[0][0][3]))



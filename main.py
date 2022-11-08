# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

if __name__ == '__main__':
    with open('traffic.txt', 'r') as file:
        packetList = []
        cycleList = []
        line = file.readlines()
        for i in range(len(line)):
            bitword = line[i].split(" ")
            cycle = int(bitword[0])
            src = bin(int(bitword[1])).replace("0b", "")
            dest = bin(int(bitword[2])).replace("0b", "")
            loadbits = bitword[3]
            header = "00" + src + dest + bin(random.getrandbits(28)).replace("0b", "")
            payload = []
            for j in range(3):
                payload.append("01" + loadbits[j * 32:(j + 1) * 32])
            tail = "11" + bin(random.getrandbits(32)).replace("0b", "")
            cycleList.append(cycle)
            packet = [header, payload[0], payload[1], payload[2], tail]
            packetList.append(packet)

            print(header + "\n" + payload[0] + "\n" + payload[1] + "\n" + payload[2] + "\n" + tail)







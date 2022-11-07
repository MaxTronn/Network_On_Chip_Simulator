# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time



    # def clock(self):
    #     tm = time.time()
    #     endTime = time.time() + 20
    #     i = 0
    #     while time.time() < endTime:
    #         i = i+1




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
            header = bin(random.getrandbits(28)).replace("0b", "") + dest + src + "00"
            payload = []
            for j in range(3):
                payload.append(loadbits[j * 32:(j + 1) * 32] + "01")
            tail = bin(random.getrandbits(32)).replace("0b", "") + "11"
            cycleList.append(cycle)
            packet = [header, payload[0], payload[1], payload[2], tail]
            packetList.append(packet)

            print(header + "\n" + payload[0] + "\n" + payload[1] + "\n" + payload[2] + "\n" + tail)



import random
import noc

if __name__ == '__main__':
    
    # Reading traffic file data

    with open('traffic.txt', 'r') as file:
        packetList = []
        cycleList = []
        
        # Reading each line of the file 
        line = file.readlines()

        #array used for converting decimal to binary
        decto2bin = ['00', '01', '10', '11']
        
        for i in range(len(line)): #Traversal of each line
            min_ind = i
            cyclei = int(line[min_ind].split(" ")[0])
            for j in range(i+1, len(line)):
                cyclej = int(line[j].split(" ")[0])
                if cyclei > cyclej:
                    min_ind = j

            line[i], line[min_ind] = line[min_ind], line[i]

        for i in range(len(line)): #Traversal of each line
            bitword = line[i].split(" ")

            cycle = int(bitword[0])
            src = decto2bin[int(bitword[1])]
            dest = decto2bin[int(bitword[2])]
            loadbits = bitword[3]
            header = "00" + src + dest + bin(random.getrandbits(28)).replace("0b", "")
            payload = [] #Creating payload
            for j in range(3):
                payload.append("01" + loadbits[j * 32:(j + 1) * 32])
            tail = "11" + bin(random.getrandbits(32)).replace("0b", "")
            cycleList.append(cycle)
            packet = [header, payload[0], payload[1], payload[2], tail]
            packetList.append(packet)

            # printing a packet's content (flits)
            print(header + " " + payload[0] + " " + payload[1] + " " + payload[2] + " " + tail+"\n")

    noc_obj = noc.Noc('XY', cycleList, packetList) #Creating a NoC object
    noc_obj.start_communication() #Starting communication
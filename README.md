# Network_On_Chip_Simulator

Main File:

1. orders the traffic data in ascending order of cycle number.
2. Traffic file's lines are traversed to create a list of packets, and their corresponding cycle numbers - and fed to the NOC Router
3. The start_communication() function of the NOC class exploits the attributes of the NoC mesh to establish the port connections and write the result into the log file.

NoC File:

1. Initialises the router objects and defines port connections between them.
2. The packets are accessed and header flit is stored in the processing element port of the source router.
3. The routing path is established based on the source and destination info obtained from the packet_list.
4. Data is buffered into a router port, every cycle, and the action is written into the Log file.
5. The buffer of the accessed router ports are emptied before the access of the subsequent packets.

Traffic File:

1. A line is ordered as follows:
    <cycle number(integer)> <space> <source router(integer)> <space> <destination router(integer)> <space> <32-bit payload(string of 32 bits)>
2. Encoding of routers:
   0: A
   1: B
   2: D
   3: C

readLog File:

1. Reads the Log file "populate.log" and creates the required plots:
   i)  Number of packets sent as a function of connections.
   ii) Latency as a function of packets sent.
   

    i:   
        1. port accesses are counted from the info present in the log file.
       
        2. There are 8 port connections, namely:
            a-b
            b-c
            c-d
            d-a
            processing-element-to-router port of every router
    ii:
        1. index of first occurence(flit placed in processing element buffer of source router) and last occurence(destination reached) of each packet is noted.

        2. This data is used to calculate number of cycles taken to route the packet in the mesh, from source to destination router.

Switch Allocator:
    1.Switch Allocator provides control information to the crossbar.   
    2.Triggered for Header/Tail flits only.   
    3.It sets connections for the crossbar after checking type and destination.   
    4.Also disconnects ports once tail flit has reached destination.   
    5.Works for both 'XY' and 'YX' routing algorithms.   
    
    
    
write xbar, port


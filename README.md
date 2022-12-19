# Network_On_Chip_Simulator


traffic File:

1. A line is ordered as follows:
    <cycle number(integer)> <space> <source router(integer)> <space> <destination router(integer)> <space> <32-bit payload(string of 32 bits)>
2. Encoding of routers:
   0: A
   1: B
   2: D
   3: C


main File:

1. orders the traffic data in ascending order of cycle number.
2. Traffic file's lines are traversed to create a list of packets, and their corresponding cycle numbers - and fed to the NOC Router
3. The start_communication() function of the NOC class exploits the attributes of the NoC mesh to establish the port connections and write the result into the log file.


noc File:

1. Initialises the router objects and defines port connections between them.
2. The packets are accessed and header flit is stored in the processing element port of the source router.
3. The routing path is established based on the source and destination info obtained from the packet_list.
4. Data is buffered into a router port, every cycle, and the action is written into the Log (populate.log) file.
5. The buffer of the accessed router ports are emptied before the access of the subsequent packets.


router File:

1. The Router class has attributes of: Ports, Switch Allocator, and Crossbar
2. The path followed by the flits for each packet - is stored in the routing_path_ports class variable of class Router.
3. create_routing_path() function is recursively called until the header flit reaches destination router.
4. Thus, a path is established for the other flits of the packet to follow until they too reach the destination.  
5. Routing path ports is emptied after routing each packet (in start_communication() function of NoC class).


switchallocator File:

1. Switch Allocator provides control information to the crossbar.   
2. Triggered for Header/Tail flits only.   
3. It sets connections for the crossbar after checking type and      destination.   
4. Also disconnects ports once tail flit has reached destination.   
5. Works for both 'XY' and 'YX' routing algorithms.   
    
    
crossbar File:

1. Crossbar is the physical connection between the inputs and outputs of NoCs.
2. It is triggered for every cycle.
3. It connects the ports of the routers based on the control information provided by the switch allocator.
4. It also disconnects the ports once the tail flit has reached the destination router.


port File:

1. port contains a buffer queue which stores the incoming flits.
2. It is used to transmit flits via this buffer mentioned above.


readLog File:

Reads the Log file "populate.log" and creates the required plots:
   i) Number of packets sent as a function of connections.
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



To run the code, the traffic file should be present in the same directory as the code files. The traffic file should be named "traffic.txt", and the log file will be named "populate.log". Run the "main.py" file and outputs will be visible on the terminal. To check the graph plots, run the "readLog.py" file, and the plots will be depicted.
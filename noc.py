import router
logFile = open("populate.txt", 'w', newline='')
class Noc :

    # router_list = [[],[]]  # Routers [[A,B],[C,D]]
    # packet_list = []
    # routing_path_ports = []
    # routing_path_routers = []

    def __init__(self, routing_algo, cycle_list, packet_list) :

        self.routing_algo = routing_algo
        self.cycle_list = cycle_list
        self.packet_list = packet_list
        self.router_list = [[],[]]

        self.initialize_router_list()
        self.mesh_connect()

    # This function initilialises the router objects and defines connections between them.
    def initialize_router_list(self):
        
        self.router_list[0].append(router.Router(self.routing_algo, "A"))
        self.router_list[0].append(router.Router(self.routing_algo, "B"))

        self.router_list[1].append(router.Router(self.routing_algo, "D"))
        self.router_list[1].append(router.Router(self.routing_algo, "C"))

        self.router_list[0][0].set_router_list(self.router_list)
        self.router_list[0][1].set_router_list(self.router_list)
        self.router_list[1][1].set_router_list(self.router_list)
        self.router_list[1][0].set_router_list(self.router_list)

        # Defining connections
    def mesh_connect(self):

        # A -- B Connection
        self.router_list[0][0].east.connect(self.router_list[0][1].west)
        self.router_list[0][1].west.connect(self.router_list[0][0].east)

        # B -- C Connection
        self.router_list[0][1].south.connect(self.router_list[1][1].north)
        self.router_list[1][1].north.connect(self.router_list[0][1].south)

        # C -- D Connection
        self.router_list[1][0].east.connect(self.router_list[1][1].west)
        self.router_list[1][1].west.connect(self.router_list[1][0].east)

        # A -- D Connection
        self.router_list[0][0].south.connect(self.router_list[1][0].north)
        self.router_list[1][0].north.connect(self.router_list[0][0].south)

    def print_routing_path_ports(self):
        for prt in router.Router.routing_path_ports :
            print(prt.owner_router.name + " " + prt.name)

        router.Router.routing_path_ports = []

    def start_communication(self):
        for i in range(len(self.packet_list)):

            # s1 and s2 are the bits for source router
            s1 = int(self.packet_list[i][0][2])
            s2 = int(self.packet_list[i][0][3])
            d1 = int(self.packet_list[i][0][4])
            d2 = int(self.packet_list[i][0][5])

            # place the packet in buffer of proc_ele port in source router
            self.router_list[s1][s2].proc_ele.buffer.put(self.packet_list[i][0])

            # create routing path
            self.router_list[s1][s2].create_routing_path(self.router_list[s1][s2].proc_ele)

            # currently, buffers of all elements are empty



            # Place the packet in the buffer of proc_ele of source router
            for j in range(5):
                self.router_list[s1][s2].proc_ele.buffer.put(self.packet_list[i][j])

            print("Packet placed in buffer of source router")
                # for k in range(len(router.Router.routing_path_ports)-1):
                #     router.Router.routing_path_ports[k+1].buffer.put(router.Router.routing_path_ports[i].buffer.get())

            start_cycle = self.cycle_list[i]
            for j in range(5) :
                cur_cycle = start_cycle + j

                for k in range( len(router.Router.routing_path_ports) - 1 ) :
                    source_port = router.Router.routing_path_ports[k]
                    dest_port = router.Router.routing_path_ports[k+1]

                    dest_port.buffer.put(source_port.buffer.get())
                    cur_cycle += 1

                    string = str(int(cur_cycle)) + ": ROUTER " + \
                             dest_port.owner_router.name + "." + dest_port.name + "  FROM: "\
                             +  source_port.owner_router.name + "." + source_port.name   +                                               \
                             "  RECEIVED FLIT: " + self.packet_list[i][j] + " FLIT NUMBER : " + str(j) + "\n"
                    print(string)
                    logFile.write(string)



            # for j in range(5):
            #
            #     string = str(int(self.cycle_list[i] + j) + len(router.Router.routing_path_ports))+": ROUTER "+ self.router_list[d1][d2].name + " RECEIVED FLIT: " +self.router_list[s1][s2].proc_ele.buffer.get()+"\n"
            #     print(string)
            #     logFile.write(string)
            # print("hi")


            #self.print_routing_path_ports()
        logFile.close()
            





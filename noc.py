import router

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
            print(prt.owner_router.name +  " " +  prt.name)

    def start_communication(self):
        for packet in self.packet_list:

            # s1 and s2 are the bits for source router
            s1 = int(packet[0][2])
            s2 = int(packet[0][3])

            # place the packet in buffer of proc_ele port in source router
            for i in range(5) :
                self.router_list[s1][s2].proc_ele.buffer.put(packet[i])

            self.router_list[s1][s2].create_routing_path(self.router_list[s1][s2].proc_ele)

            # here we need a return statement from the router called to signify packet has been transmitted

            self.print_routing_path_ports()

            





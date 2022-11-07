import Router

class NOC :

    router_list = [[],[]]  # Routers [[A,B],[D,C]]
    packet_list = []

    def __init__(self, traffic_file, routing_algo, latency, cycle_list, packet_list) :
        self.latency = latency
        self.traffic_file = traffic_file
        self.routing_algo = routing_algo
        self.cycle_list = cycle_list
        self.packet_list = packet_list

    # This function initilialises the router objects and defines connections between them.
    # def initialize_router_list(self):
    #     for i in range(4) :
    #         self.router_list.append(Router())
def initialize_router_list(self):
         for i in range(4) :
             self.router_list.append(Router())

        # Defining connections
def mesh_connect(self):
        # A -- B Connection
        self.router_list[0][0].east = self.router_list[0][1].west
        self.router_list[0][1].west = self.router_list[0][0].east

        # B -- C Connection
        self.router_list[0][1].south = self.router_list[1][1].north
        self.router_list[1][1].north = self.router_list[0][1].south

        # C -- D Connection
        self.router_list[1][0].east = self.router_list[1][1].west
        self.router_list[1][1].west = self.router_list[1][0].east

        # A -- D Connection
        self.router_list[0][0].south = self.router_list[1][0].north
        self.router_list[1][0].north = self.router_list[0][0].south


    # This function handles the communication part of the NOC
    def start_communication(self):
        

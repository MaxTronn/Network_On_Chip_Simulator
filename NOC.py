class NOC :

    router_list = []  # Routers [A,B,C,D]
    packet_list = []


    def __init__(self, traffic_file, routing_algo, latency, cycle_list, packet_list) :
        self.latency = latency
        self.traffic_file = traffic_file
        self.routing_algo = routing_algo
        self.cycle_list = cycle_list
        self.packet_list = packet_list

    # This function initilialises the router objects and defines connections between them.
    def initialize_router_list(self):
        for i in range(4) :
            self.router_list.append(Router())

        # Defining connections

        # A -- B Connection
        self.router_list[0].east = self.router_list[1]
        self.router_list[1].west = self.router_list[0]

        # B -- C Connection
        self.router_list[1].south = self.router_list[2]
        self.router_list[2].north = self.router_list[1]

        # C -- D Connection
        self.router_list[2].east = self.router_list[3]
        self.router_list[3].west = self.router_list[2]

        # A -- D Connection
        self.router_list[0].south = self.router_list[3]
        self.router_list[3].north = self.router_list[0]


    # This function handles the communication part of the NOC
    def start_communication(self):
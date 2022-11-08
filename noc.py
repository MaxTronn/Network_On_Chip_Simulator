import router

class Noc :

    router_list = [[],[]]  # Routers [[A,B],[C,D]]
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
            self.router_list.append(router())

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

    def start_communication(self):
        for p in range(self.packet_list):
            s1=0
            s2=0
            for f in range(self.packet_list[p]):
                if(f==0):
                    s1=self.packet_list[p][f][2]
                    s2=self.packet_list[p][f][3]
                    s1=int(s1)
                    s2=int(s2)
                    self.router_list[s1][s2].proc_ele.buffer.put(self.packet_list[p][f])
                else: 
                    self.router_list[s1][s2].proc_ele.buffer.put(self.packet_list[p][f])

            





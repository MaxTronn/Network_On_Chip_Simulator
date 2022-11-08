# Switch Allocator provides control information to the crossbar

# Switch Allocator works only when there is a header flit or a tail flit


from queue import Queue
from noc import Noc
from crossbar import Crossbar


class SwitchAllocator:


    def __init__(self, north, south, east, west, proc_ele, routing_algo, owner_router):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.proc_ele = proc_ele

        self.routing_algo = routing_algo
        self.owner_router = owner_router


    # This function is called for the header flit to make connections in the crossbar
    def connect_ports(self, source_port):

        flit = source_port.buffer.front()

        # Figure out the destination router using header flit
        # 00 = A
        # 01 = B
        # 11 = C
        # 10 = D

        dest_bit_0 = flit[4]
        dest_bit_1 = flit[5]

        # If the current router is the destination router, send the flit to Proc_ele port
        if(Noc.router_list[dest_bit_1][dest_bit_0] == self.owner_router) :
            self.owner_router.Crossbar.connect(source_port, self.proc_ele)

        # Search if adjacent router is the destination router
        elif(self.north != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.north.connected_router_port.owner_router) :
            self.owner_router.Crossbar.connect(source_port, self.north)

        elif(self.south != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.south.connected_router_port.owner_router) :
            self.owner_router.Crossbar.connect(source_port, self.south)

        elif (self.east != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.east.connected_router_port.owner_router):
            self.owner_router.Crossbar.connect(source_port, self.east)

        elif (self.west != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.west.connected_router_port.owner_router):
            self.owner_router.Crossbar.connect(source_port, self.west)

        else :
            #If ajacent router is not destination router, send to the next router as per routing algo
            if(self.routing_algo == 'XY') :
                if(self.east != None) :
                    self.owner_router.Crossbar.connect(source_port, self.east)

                else:
                    self.owner_router.Crossbar.connect(source_port, self.west)

            else : # routing_algo == 'YX'
                if (self.north != None):
                    self.owner_router.Crossbar.connect(source_port, self.north)

                else:
                    self.owner_router.Crossbar.connect(source_port, self.south)


    # This function is called when the tail flit arrives at the router
    def disconnect_ports(self):
        self.owner_router.Crossbar.terminate_connections()

    # def reallocate(self, source, destination):
    #
    #     self.src = source
    #     self.dest = destination
    #
    #     if self.src == '00' and self.dest == '10':
    #         router_list[1].west = router_list[0].east
    #         router_list[1].south = router_list[1].west
    #         router_list[2].north = router_list[1].south
    #
    #     elif self.src == '01' and self.dest == '11':
    #         router_list[0].east = router_list[1].west
    #         router_list[0].south = router_list[0].east
    #         router_list[3].north = router_list[0].south
    #
    #     elif self.src == '10' and self.dest == '00':
    #         router_list[3].east = router_list[2].west
    #         router_list[3].north = router_list[3].east
    #         router_list[0].south = router_list[3].north
    #
    #     elif self.src == '11' and self.dest == '01':
    #         router_list[2].west = router_list[3].east
    #         router_list[2].north = router_list[2].west
    #         router_list[1].south = router_list[2].north



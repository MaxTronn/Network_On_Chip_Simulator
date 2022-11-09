# Switch Allocator provides control information to the crossbar

# Switch Allocator works only when there is a header flit or a tail flit


from queue import Queue
from noc import Noc
from crossbar import Crossbar


class SwitchAllocator:


    def __init__(self, routing_algo, owner_router):
        self.owner_router = owner_router
        self.proc_ele = owner_router.proc_ele
        self.routing_algo = owner_router.routing_algo


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
            self.owner_router.Crossbar.connect(source_port, self.owner_router.proc_ele)

        # Search if adjacent router is the destination router
        elif(self.north != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.owner_router.north.connected_router_port.owner_router) :
            self.owner_router.Crossbar.connect(source_port, self.owner_router.north)


        elif(self.south != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.owner_router.south.connected_router_port.owner_router) :
            self.owner_router.Crossbar.connect(source_port, self.owner_router.south)


        elif (self.east != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.owner_router.east.connected_router_port.owner_router):
            self.owner_router.Crossbar.connect(source_port, self.owner_router.east)


        elif (self.west != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.owner_router.west.connected_router_port.owner_router):
            self.owner_router.Crossbar.connect(source_port, self.owner_router.west)

        else :
            #If ajacent router is not destination router, send to the next router as per routing algo
            if(self.routing_algo == 'XY') :
                if(self.east != None) :
                    self.owner_router.Crossbar.connect(source_port, self.owner_router.east)


                else:
                    self.owner_router.Crossbar.connect(source_port, self.owner_router.west)


            else : # routing_algo == 'YX'
                if (self.north != None):
                    self.owner_router.Crossbar.connect(source_port, self.owner_router.north)

                else:
                    self.owner_router.Crossbar.connect(source_port, self.owner_router.south)


    # This function is called when the tail flit arrives at the router
    def disconnect_ports(self):
        self.owner_router.Crossbar.terminate_connections()



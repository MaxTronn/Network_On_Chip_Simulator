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

        head_flit = source_port.buffer.front()
        reached_dest = False
        # Figure out the destination router using header flit
        # 00 = A
        # 01 = B
        # 11 = C
        # 10 = D

        dest_bit_0 = head_flit[4]
        dest_bit_1 = head_flit[5]

        # If the current router is the destination router, send the flit to Proc_ele port
        if(Noc.router_list[dest_bit_1][dest_bit_0] == self.owner_router) :
            self.owner_router.Crossbar.connect(source_port, self.owner_router.proc_ele)
            return True

        # Search if adjacent router is the destination router
        elif(self.owner_router.north != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.owner_router.north.connected_router_port.owner_router) :
            self.owner_router.Crossbar.connect(source_port, self.owner_router.north.connected_router_port)


        elif(self.owner_router.south != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.owner_router.south.connected_router_port.owner_router) :
            self.owner_router.Crossbar.connect(source_port, self.owner_router.south.connected_router_port)


        elif (self.owner_router.east != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.owner_router.east.connected_router_port.owner_router):
            self.owner_router.Crossbar.connect(source_port, self.owner_router.east.connected_router_port)


        elif (self.owner_router.west != None and Noc.router_list[dest_bit_1][dest_bit_0] == self.owner_router.west.connected_router_port.owner_router):
            self.owner_router.Crossbar.connect(source_port, self.owner_router.west.connected_router_port)

        else :
            #If ajacent router is not destination router, send to the next router as per routing algo
            if(self.routing_algo == 'XY') :
                if(self.owner_router.east != None) :
                    self.owner_router.Crossbar.connect(source_port, self.owner_router.east.connected_router_port)

                else:
                    self.owner_router.Crossbar.connect(source_port, self.owner_router.west.connected_router_port)


            else : # routing_algo == 'YX'
                if (self.owner_router.north != None):
                    self.owner_router.Crossbar.connect(source_port, self.owner_router.north.connected_router_port)

                else:
                    self.owner_router.Crossbar.connect(source_port, self.owner_router.south.connected_router_port)

        return reached_dest

    # This function is called when the tail flit arrives at the router
    def disconnect_ports(self):
        self.owner_router.Crossbar.terminate_connections()



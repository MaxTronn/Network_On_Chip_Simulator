# Switch Allocator provides control information to the crossbar

# Switch Allocator works only when there is a header flit or a tail flit


import queue
from crossbar import Crossbar


class SwitchAllocator:


    def __init__(self, owner_router):
        self.owner_router = owner_router
        self.proc_ele = owner_router.proc_ele
        self.routing_algo = owner_router.routing_algo
        self.router_list = None

    def set_router_list(self, router_list):
        self.router_list = router_list

    # This function is called for the header flit to make connections in the crossbar
    def connect_ports(self, source_port):
        q = source_port.buffer
        head_flit = q.queue[0]
        reached_dest = False
        # Figure out the destination router using header flit
        # 00 = A
        # 01 = B
        # 11 = C
        # 10 = D

        dest_bit_1 = int(head_flit[4])
        dest_bit_0 = int(head_flit[5])

        # If the current router is the destination router, send the flit to Proc_ele port
        if(self.router_list[dest_bit_1][dest_bit_0] == self.owner_router) :
            self.owner_router.crossbar.connect(source_port, self.owner_router.proc_ele)
            return True

        # Search if adjacent router is the destination router
        elif(self.owner_router.north.connected_router_port != None and self.router_list[dest_bit_1][dest_bit_0] == self.owner_router.north.connected_router_port.owner_router) :
            self.owner_router.crossbar.connect(source_port, self.owner_router.north.connected_router_port)


        elif(self.owner_router.south.connected_router_port != None and self.router_list[dest_bit_1][dest_bit_0] == self.owner_router.south.connected_router_port.owner_router) :
            self.owner_router.crossbar.connect(source_port, self.owner_router.south.connected_router_port)


        elif (self.owner_router.east.connected_router_port != None and self.router_list[dest_bit_1][dest_bit_0] == self.owner_router.east.connected_router_port.owner_router):
            self.owner_router.crossbar.connect(source_port, self.owner_router.east.connected_router_port)


        elif (self.owner_router.west.connected_router_port != None and self.router_list[dest_bit_1][dest_bit_0] == self.owner_router.west.connected_router_port.owner_router):
            self.owner_router.crossbar.connect(source_port, self.owner_router.west.connected_router_port)

        else :
            #If ajacent router is not destination router, send to the next router as per routing algo
            if(self.routing_algo == 'XY') :
                if(self.owner_router.east.connected_router_port != None) :
                    self.owner_router.crossbar.connect(source_port, self.owner_router.east.connected_router_port)

                else:
                    self.owner_router.crossbar.connect(source_port, self.owner_router.west.connected_router_port)


            else : # routing_algo == 'YX'
                if (self.owner_router.north.connected_router_port != None):
                    self.owner_router.crossbar.connect(source_port, self.owner_router.north.connected_router_port)

                else:
                    self.owner_router.crossbar.connect(source_port, self.owner_router.south.connected_router_port)

        return reached_dest

    # This function is called when the tail flit arrives at the router
    def disconnect_ports(self):
        self.owner_router.crossbar.terminate_connections()
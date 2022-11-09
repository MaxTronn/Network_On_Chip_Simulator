import port
import switchallocator
import crossbar


class Router:

    def __init__(self, routing_algo):
        self.crossbar = crossbar.Crossbar()
        self.north = port.Port()
        self.south = port.Port()
        self.east = port.Port()
        self.west = port.Port()
        self.proc_ele = port.Port()
        self.switch_allocator = switchallocator.SwitchAllocator(routing_algo, self)

    # This function creates the routing path
    def create_routing_path(self, data_port):
        # Switch allocator connects the input port to output port using crossbar
        self.switch_allocator.connect_ports(data_port)

        # Header flit is now transmitted to the connected port of next router
        # Now, next router needs to further create the routing path
        self.crossbar.output_port.owner_router.create_routing_path(self.crossbar.output_port)
        # B.west.owner_router.create_routing_path(B.west)
        # C.north.owner_router.create_routing_path(C.north)

    def flit_classifier(self, curr_flit):
        flit_type_bit = curr_flit[:2]

        if flit_type_bit == '00':

        elif flit_type_bit == '01':

        else:

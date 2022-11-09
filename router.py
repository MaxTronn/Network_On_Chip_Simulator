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

    def transmit_packet(self):
        # Switch allocator connects the proc_ele port and port of the next router
        self.switch_allocator.connect_ports(self.proc_ele)

        # Data is now transmitted to the connected port of next router
        # Now, next router needs to further transmit the data
        self.switch_allocator.destination_port.owner_router.crossbar.transfer_data()

    def flit_classifier(self, curr_flit):
        flit_type_bit = curr_flit[:2]

        if flit_type_bit == '00':

        elif flit_type_bit == '01':

        else:

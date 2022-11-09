import port
import switchallocator
import crossbar
from noc import Noc

class Router:

    def __init__(self, routing_algo,name):
        self.crossbar = crossbar.Crossbar()
        self.north = port.Port(self, "north")
        self.south = port.Port(self, "south")
        self.east = port.Port(self, "east")
        self.west = port.Port(self, "west")
        self.proc_ele = port.Port(self, "proc_ele")
        self.switch_allocator = switchallocator.SwitchAllocator(routing_algo, self)
        self.name = name

    # This function creates the routing path
    def create_routing_path(self, data_port):
        # Switch allocator connects the input port to output port using crossbar
        reached_dest = self.switch_allocator.connect_ports(data_port)

        # Header flit is now transmitted to the connected port of next router
        # Now, next router needs to further create the routing path
        if not reached_dest:
            self.crossbar.output_port.owner_router.create_routing_path(self.crossbar.output_port)
        # B.west.owner_router.create_routing_path(B.west)  --> B.create_routing_path(B.west)
        # C.north.owner_router.create_routing_path(C.north)  --> C.create_routing_path(C.north)

        else : # If proc_ele of destination router is reached, we remove the header_flit from its buffer
            # Now routing path is created
            # Now we send the packet (including header_flit) through the routing path and count cycles alongside.
            Noc.routing_path_ports.append(self.crossbar.output_port)
            self.crossbar.output_port.buffer.get()

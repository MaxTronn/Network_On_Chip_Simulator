# switch allocator needs to be called every cycle where flit transfer through a particular router needs to takes place.
# At each decisive cycle the reallocate() function reallocates the input and output ports of the XBar and returns the
# ports that need to be enabled by the XBar for that cycle
import crossbar

router_list = ['A', 'B', 'C', 'D']


class SwitchAllocator:
    xbar = crossbar.Crossbar()

    def __init__(self, ports):
        self.routing = 'XY'
        self.src = None
        self.dest = None

    def reallocate(self, source, destination):

        self.src = source
        self.dest = destination

        if self.src == '00' and self.dest == '10':
            router_list[1].west = router_list[0].east
            router_list[1].south = router_list[1].west
            router_list[2].north = router_list[1].south

        elif self.src == '01' and self.dest == '11':
            router_list[0].east = router_list[1].west
            router_list[0].south = router_list[0].east
            router_list[3].north = router_list[0].south

        elif self.src == '10' and self.dest == '00':
            router_list[3].east = router_list[2].west
            router_list[3].north = router_list[3].east
            router_list[0].south = router_list[3].north

        elif self.src == '11' and self.dest == '01':
            router_list[2].west = router_list[3].east
            router_list[2].north = router_list[2].west
            router_list[1].south = router_list[2].north

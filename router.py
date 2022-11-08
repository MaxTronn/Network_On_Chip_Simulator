import port
import switchallocator
import crossbar


class Router:

    def __init__(self):
        self.switch_allocator = switchallocator.SwitchAllocator()
        self.crossbar = crossbar.Crossbar()
        self.north = port.Port()
        self.south = port.Port()
        self.east = port.Port()
        self.west = port.Port()

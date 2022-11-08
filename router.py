class Router:

    def __init__(self):
        self.inp = 10
        self.out = 10
        # Temporary Storage (buffer) for the router
        self.temp_store = format(0, '#036b').replace("0b", "")
        self.north = None
        self.south = None
        self.east = None
        self.west = None

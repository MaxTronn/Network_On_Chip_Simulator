
class Router:

    def __init__(self, connections, inp, out):
        self.inp = 10
        self.out = 10
        self.connection = connections
        # Temporary Storage (buffer) for the router
        self.temp_store = format(0, '#036b').replace("0b", "")
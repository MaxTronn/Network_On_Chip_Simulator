from queue import Queue


class Port:

    def __init__(self, owner_router, name):
        self.buffer = Queue(maxsize=5)
        self.connected_router_port = None
        self.owner_router = owner_router
        self.name = self.name

    def send_to_port(self, incoming_flit):
        self.buffer.put(incoming_flit)

    def send_from_port(self):
        return self.buffer.get()

    def connect(self, router_port):
        self.connected_router_port = router_port


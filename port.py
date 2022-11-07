from queue import Queue
class port:
    def __init__(self):
        self.port_buffer=Queue(maxsize=5)

    def send_to_port(self, incoming_flit):
        self.port_buffer.put(incoming_flit)
    
    def send_from_port(self, outgoing_flit):
        return self.port_buffer.get

        

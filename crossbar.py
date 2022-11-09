class Crossbar:
    def __init__(self):
        self.input_port = None
        self.output_port = None

    def connect(self, input_port, output_port):
        self.input_port = input_port
        self.output_port = output_port
        self.transfer_data()

    def transfer_data(self):
        self.output_port.buffer.put(self.input_port.buffer.get())


    def terminate_connections(self):
        self.input_port = None
        self.output_port = None



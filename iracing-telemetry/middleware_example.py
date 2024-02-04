class Middleware:
    def process(self, data):
        # Process the data and return it
        return data

class Server:
    def __init__(self):
        self.middlewares = []

    def use_middleware(self, middleware):
        self.middlewares.append(middleware)

    def loop(self, data_buffer):
        for middleware in self.middlewares:
            data_buffer = middleware.process(data_buffer)
        # Proceed with the rest of the loop using the processed data_buffer

# Example middleware usage
class CustomMiddleware(Middleware):
    def process(self, data):
        # Custom processing
        return data

server = Server()
server.use_middleware(CustomMiddleware())
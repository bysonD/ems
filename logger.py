class Handler:
    def send(self, message):
        raise NotImplemented
    
class ConsoleHandler(Handler):
    def send(self, message):
        print(message)

class FileHandler(Handler):
    def __init__(self, path):
        self.path = path

    def send(self, message):
        with open(self.path, "a") as f:
            f.write(message)

class Logger:
    def __init__(self, handler):
        self.handler = handler

    def log(self, message):
        self.handler.send(message)

logger = Logger(ConsoleHandler())
logger.log("Test Message")
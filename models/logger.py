import datetime as dt

LOG_FOLDER_NAME = "logs"

class Handler:
    def send(self, message):
        raise NotImplemented
    
    @staticmethod
    def file_path_formatter():
        current_date = dt.datetime.now()
        formatted = current_date.strftime("%Y_%m_%d_")
        return f"logs/{formatted + LOG_FOLDER_NAME}.log"
    
    @staticmethod
    def date_message_formatter():
        current_date = dt.datetime.now()
        formatted = current_date.strftime("[Date: %Y/%m/%d Time: %H:%M:%S]")
        return formatted

class ComboHandler(Handler):
    def send(self, message):
        formatted = Handler.date_message_formatter()
        print(f"{formatted}\n{message}\n")

        file_path = Handler.file_path_formatter()
        full_message = f"{formatted} -> {message}"
        with open(file_path, "a") as f:
            f.write(f"{full_message}\n")

class Logger:
    def __init__(self, handler):
        self.handler = handler

    def log(self, message):
        self.handler.send(message)

DEF_LOGGER = Logger(ComboHandler())

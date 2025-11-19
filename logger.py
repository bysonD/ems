import datetime as dt

LOG_FILE_NAME = "logs"

class Handler:
    def send(self, message):
        raise NotImplemented

class ComboHandler(Handler):
    def send(self, message):
        current_date = dt.datetime.now()
        formatted = current_date.strftime("[Date: %Y/%m/%d Time: %H:%M:%S]")
        full_message = f"{formatted} -> {message}"
        print(full_message)

        formatted_date = current_date.strftime("%Y_%m_%d_")
        final_path = f"Logs/{formatted_date + LOG_FILE_NAME}.log"
        with open(final_path, "a") as f:
            f.write(full_message)

class Logger:
    def __init__(self, handler):
        self.handler = handler

    def log(self, message):
        self.handler.send(message)

DEF_LOGGER = Logger(ComboHandler())
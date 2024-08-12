import json
import logging
import os
from logging import Formatter, FileHandler

def create_log_dir():
    try:
        if not os.path.exists("logs"):
            os.makedirs("logs")
    except OSError as e:
        raise Exception("Error: Failed to create the log directory.") from e


class JsonFormatter(Formatter):
    def __init__(self):
        super(JsonFormatter, self).__init__()

    def format(self, record):
        json_record = {}
        json_record["message"] = record.getMessage()
        if "timestamp" in record.__dict__:
            json_record["timestamp"] = record.__dict__["timestamp"]
        if "req" in record.__dict__:
            json_record["req"] = record.__dict__["req"]
        if "res" in record.__dict__:
            json_record["res"] = record.__dict__["res"]
        if record.levelno == logging.ERROR and record.exc_info:
            json_record["err"] = self.formatException(record.exc_info)
        return json.dumps(json_record)


create_log_dir()

# 로거 설정
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# 핸들러와 포매터 설정
handler = FileHandler("logs/output.log")
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)

logging.getLogger("uvicorn.access").disabled = True

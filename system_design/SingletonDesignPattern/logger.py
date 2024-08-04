
from log_builder import LogBuilder

class Logger(LogBuilder):
    def __init__(self):
        pass 

    @staticmethod
    def info(msg: str) -> None:
        print(msg)

    @staticmethod
    def warn(msg: str) -> None:
        print(msg)

    @staticmethod
    def error(msg: str) -> None:
        print(msg)
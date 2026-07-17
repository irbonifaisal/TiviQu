from encoder.config import APP_NAME, VERSION
from encoder.utils.logger import Logger


def main():

    Logger.line()

    print(APP_NAME)
    print("Version :", VERSION)

    Logger.line()

    print()
    Logger.success("Foundation Loaded")
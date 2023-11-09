import logging
import datetime
import os
import sys


# This class provides logging functionality for the test framework.

class MyLogger:
    logger_initialized = False

    def __init__(self):
        self.class_name = self.__class__.__name__
        if not MyLogger.logger_initialized:
            MyLogger.initialize_logger()
            MyLogger.logger_initialized = True
        self.logger = logging.getLogger('my_logger')

    @staticmethod
    def initialize_logger():
        root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../logs'))
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"TestSession_{timestamp}.log"
        log_file_path = os.path.join(root_directory, file_name)
        if not os.path.exists(root_directory):
            os.makedirs(root_directory)

        logger = logging.getLogger('my_logger')
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)

        # Include the %(name)s placeholder in the log message format
        formatter = logging.Formatter("[%(asctime)s,%(msecs)03d] - [%(levelname)-7s] - [%(module)-12s] - [%(funcName)s] - %(message)s", "%Y-%m-%d %H:%M:%S")

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
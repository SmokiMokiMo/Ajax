import logging
import datetime
import os
import sys

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
        logger.setLevel(logging.DEBUG)  # Set the log level to the desired level

        # Create a file handler for writing log messages to a file
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler for displaying log messages in the console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)  # Set the console log level (you can adjust it)

        formatter = logging.Formatter("[%(asctime)s,%(msecs)03d] - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        
# log = MyLogger()
# log.logger.info("test")
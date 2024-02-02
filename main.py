import random
import logging
import ecs_logging


LOG_LEVEL = 'DEBUG'


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    # Create handlers
    c_handler = logging.FileHandler(f"log/logFile.txt")
    # Create formatters and add it to handlers
    # Configure the logger
    c_handler.setFormatter(ecs_logging.StdlibFormatter())
    # Add handlers to the logger
    logger.addHandler(c_handler)
    return logger


logger = get_logger(__name__)


for i in range(0, 15):
    x = random.randint(0, 2)
    if (x ==  0):
        logger.warning('Log Message')
    elif(x == 1):
        logger.critical('Log Message')
    else:
        logger.error('Log Message')
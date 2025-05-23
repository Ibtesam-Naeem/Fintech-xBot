#---------------------LOGGER CONFIGURATION---------------------#
import logging

def setup_logger(name=None, level=logging.INFO):
    """
    Sets up a modular logger with console handler for AWS Lambda.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.hasHandlers():
        logger.handlers.clear()

    # Standard format for log messages
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Adds the handler to the logger
    logger.addHandler(console_handler)

    return logger
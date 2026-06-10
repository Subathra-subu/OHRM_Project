import logging
import os


def log_generator():

    logger = logging.getLogger(__name__)

    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    log_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "test.log"
    )

    file_handler = logging.FileHandler(log_path)

    console_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)

    return logger
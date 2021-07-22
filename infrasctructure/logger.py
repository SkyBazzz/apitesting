import logging
import sys

from config import Config


def get_configured_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console_h = logging.StreamHandler(sys.stdout)
    console_h.setLevel(Config.LOG_LEVEL)
    logger.addHandler(console_h)
    return logger

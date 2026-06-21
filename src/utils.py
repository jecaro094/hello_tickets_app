import logging
from logging import Logger
from src.constants import LOGGER_FORMAT_MSG

logging.basicConfig(
    level=logging.INFO,
    format=LOGGER_FORMAT_MSG,
)

def get_logger(file_name: str) -> Logger:
    """
    Retrieves basic logger given file name
    """
    return logging.getLogger(file_name)
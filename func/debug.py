import logging
from os import get_terminal_size


def error_found(err):
    print(f"{'=' * (get_terminal_size()[0] - 1)}\nError logged:\n{err}")
    create_log_file(err)


def create_log_file(err: Exception):
    logger = logging.getLogger()
    handler = logging.FileHandler('error.log')
    logger.addHandler(handler)
    logger.error(err, exc_info=True)

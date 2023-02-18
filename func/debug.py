import logging


def create_log_file(err: Exception):
    logger = logging.getLogger()
    handler = logging.FileHandler('error.log')
    logger.addHandler(handler)
    logger.error(err, exc_info=True)

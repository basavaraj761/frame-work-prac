import logging


def test_log():
    logger = logging.getLogger(__name__)

    FileHandler = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s :%(levelname)s:%(name)s:%(message)s")
    FileHandler.setFormatter(formatter)
    logger.addHandler(FileHandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("Adebug staement is executed")
    logger.info("information statement")
    logger.debug("Adebug staement is executed")
    logger.warning("something is in warning mode")
    logger.error("Amajor error has happened")
    logger.critical("zritical Issue")

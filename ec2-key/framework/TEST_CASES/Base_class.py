import inspect
import logging


class Baseclass:

    def test_getlog(self):
        loggername=inspect.stack()[1][3]
        logger = logging.getLogger(__name__)

        FileHandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s:%(name)s:%(message)s")
        FileHandler.setFormatter(formatter)
        logger.addHandler(FileHandler)

        logger.setLevel(logging.DEBUG)

        return logger



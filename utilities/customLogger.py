import logging
import os.path


class LogGen():

    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + '..\\logs\\automation.log'
        logging.basicConfig(filename=path,
                            format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%y')
        logger= logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
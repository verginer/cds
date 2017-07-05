import logging
import os


FORMAT = '%(asctime)s  - %(name)s - %(levelname)s | %(message)s'

logging.basicConfig(level=logging.DEBUG,
                    format=FORMAT,
                    filename='logs/all.log',
                    filemode='w')


def get_logger(path: str) -> logging.Logger:
    """
    returns a logger with a proper name

    Parameters
    ----------

    path : str
        give the name of the file that invokes it

    Example
    -------

    >>> get_logger(__file__)
    <Logger rule.utils.py (DEBUG)>

    """
    long_name = os.path.basename(path)
    base = '.'.join(long_name.split('.')[-2:])
    logger = logging.getLogger('rule.' + base)
    return logger

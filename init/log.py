#!/usr/bin/env python3
import logging
from . import config


def init() -> None:
    """
    Initialize root logging in python and set logging level

    :return: None
    """

    loglevel = config.cnf['logging']['level']

    if loglevel == "debug":
        level = logging.DEBUG
    elif loglevel == "info":
        level = logging.INFO
    elif loglevel == "warning":
        level = logging.WARNING
    elif loglevel == "error":
        level = logging.ERROR
    elif loglevel == "critical":
        level = logging.CRITICAL
    else:
        level = logging.DEBUG

    logging.basicConfig(format='%(asctime)-15s » %(message)s', level=level)

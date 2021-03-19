#!/usr/bin/env python3
import argparse
from typing import Optional

args: Optional[argparse.Namespace] = None


def init() -> None:
    """
    Initialize argument parser and parse arguments into global variable "args"

    :return: None
    """
    global args

    arg = argparse.ArgumentParser(description='NastySync - A custom sync script')

    arg.add_argument('-c', '--config', default="config.ini", help="Configuration file to use")
    arg.add_argument('--write-config', action='store_true', help="Write current configuration to config file")
    arg.add_argument('--no-read-config', action='store_false', help="Skip loading configuration from disk")
    arg.add_argument('--loglevel', default='info', choices=['debug', 'info', 'warning', 'error', 'critical'],
                     help="Set loglevel to one of five levels (default: info)")

    args = arg.parse_args()

#!/usr/bin/env python3
from configparser import ConfigParser
from os import path
from typing import Optional
from . import param


cnf: Optional[ConfigParser] = None


def init() -> None:
    """
    Initialize configuration

    :return: None
    """
    global cnf
    args = param.args
    cnf = ConfigParser()

    # Add configuration options here
    cnf['DEFAULT'] = {}

    cnf['logging'] = {
        'level': param.args.loglevel
    }

    # Load config from file if it exists
    if args.no_read_config and path.isfile(args.config):
        cnf.read(args.config)

    # Write config to file if requested
    if args.write_config:
        with open(args.config, "w") as fp:
            cnf.write(fp)

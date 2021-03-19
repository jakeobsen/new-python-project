#!/usr/bin/env python3
import init as l
from time import sleep

if __name__ == '__main__':
    a, c, CONST = l.p.args, l.c.cnf, l.CONST
    print(CONST.NAME, "version", CONST.VERSION, "by", CONST.AUTHOR)
    print(CONST.COPYRIGHT, "- released under the", CONST.LICENSE, "license")
    sleep(0.01)

    # Application begins here

    l.info("System has been initialized!")
    l.info(f"Congiguration file in {a.config}")
    l.info(f"Log level set to: {c['logging']['level']}")


#!/usr/bin/env python3
from typing import Optional


CONST: Optional[object] = None


def init():
    """
    Initialize Constants

    :return: None
    """
    global CONST
    CONST = _Const()


def _constant(f) -> property:
    """ Property definition """

    def fset(self, value):
        """ Constants cannot be changed, so trying to change it will raise a TypeError """
        raise TypeError

    def fget(self):
        """ Get value of constant """
        return f(self)

    return property(fget, fset)


# noinspection PyPep8Naming
class _Const(object):

    @_constant
    def NAME(self) -> str:
        """ Constant: NAME """
        return "My Demo Application"

    @_constant
    def VERSION(self) -> str:
        """ Constant: VERSION """
        return "0.0.1"

    @_constant
    def AUTHOR(self) -> str:
        """ Constant: AUTHOR """
        return "Bob Smith"

    @_constant
    def LICENSE(self) -> str:
        """ Constant: LICENSE """
        return "GPLv2"

    @_constant
    def COPYRIGHT(self) -> str:
        """ Constant: COPYRIGHT """
        return "Copyright 2021 © Bob Smith"

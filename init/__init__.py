from . import config as c
from . import param as p
from . import log as l
from . import const
from logging import info, debug, warning, error, critical

p.init()
c.init()
l.init()
const.init()
CONST = const.CONST

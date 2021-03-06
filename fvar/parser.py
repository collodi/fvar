from .exceptions import *
from .lines import Lines
from .defmt import DeFmt

def matchline(defmt, lns):
    if lns.next() is None:
        raise MissingValue(defmt, lns)

    obj = {}
    for var in defmt.vars:
        val = lns.getvar(var.size)
        if val is None:
            raise MissingValue(defmt, lns)

        obj[var.name] = val

    return obj

def parse(fmt, filename):
    f = Lines(filename)
    defmt = DeFmt(fmt)

    obj = {}
    for _ in defmt:
        vals = matchline(defmt, f)
        obj.update(vals)

    f.close()
    return obj

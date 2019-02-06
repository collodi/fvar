import sys

from .exceptions import *
from .defmt import DeFmt

def matchline(defmt, data):
    ln = defmt.next()
    for var in defmt.vars:
        if var.name not in data:
            raise MissingVariable(defmt, var)

        ln = ln.replace('<{}>'.format(var.name), str(data[var.name]))

    return ln

def dump(fmt, data, filename=None):
    defmt = DeFmt(fmt)

    out = None
    if filename is None:
        out = sys.stdout
    else:
        out = open(filename, 'w')

    while not defmt.done:
        ln = matchline(defmt, data)
        print(ln, file=out)

    if filename is not None:
        out.close()

class InvalidFormat(Exception):
    def __init__(self, fmt):
        super().__init__('Invalid format "{}"'.format(fmt))

class MissingValues(Exception):
    def __init__(self, defmt, lns):
        expd = sum(v.size for v in defmt.vars)
        given = lns.nitems()

        fmtstr = '''\
line {}: expected {} items, but given {}.

{}
{}'''.format(lns.lineno, expd, given, defmt.line, lns.line)

        super().__init__(fmtstr)

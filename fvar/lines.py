import re

class Lines:
    def __init__(self, filename):
        self.f = open(filename, 'r')

        self.lineno = -1
        self.line = None
        self.splits = None

    def nitems(self):
        return len(self.line.split()) if self.line else 0

    def next(self):
        self.split = 0
        self.lineno += 1

        try:
            self.line = next(self.f).rstrip()
            self.splits = (
                    m.span()
                    for m in re.finditer(r'\s+|$', self.line)
            )
        except StopIteration:
            self.line = None
            self.splits = None

        return self.line

    def getvar(self, size):
        j, i = 0, 0
        for _ in range(size):
            try:
                j, i = next(self.splits)
            except StopIteration:
                return None

        v = self.line[self.split:j]
        self.split = i
        return v

    def close(self):
        self.f.close()

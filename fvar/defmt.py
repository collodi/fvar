import re

class Var:
    def __init__(self, name, size=1):
        self.name = name
        self.size = size

class DeFmt:
    def __init__(self, fmt):
        self.vars = None
        self.done = False
        self.line = None
        self.lineno = -1
        self.lines = fmt.splitlines()

    def next(self):
        if self.done:
            return None

        self.lineno += 1
        self.line = self.lines[self.lineno]
        self.vars = [
                Var(m.group(1))
                for m in re.finditer(r'<([^>]+)>', self.line)
        ]

        if self.lineno == len(self.lines) - 1:
            self.done = True

        return self.line

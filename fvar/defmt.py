import re

class Var:
    def __init__(self, name, size=1):
        self.name = name
        self.size = size

class DeFmt:
    def __init__(self, fmt):
        self.lines = fmt.splitlines()

    def is_comment(self):
        return self.lines[self.lineno].startswith('#')

    def skip_comments(self):
        while self.lineno < len(self.lines) and self.is_comment():
            self.lineno += 1

    def __iter__(self):
        self.line = None
        self.vars = None
        self.lineno = -1
        return self

    def __next__(self):
        if self.lineno >= len(self.lines):
            raise StopIteration

        self.lineno += 1
        self.skip_comments()

        if self.lineno >= len(self.lines):
            raise StopIteration

        self.line = self.lines[self.lineno]
        self.vars = [
                Var(m.group(1))
                for m in re.finditer(r'<([^>]+)>', self.line)
        ]

        return self.line

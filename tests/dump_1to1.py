from context import fvar

import os
from tempfile import NamedTemporaryFile

fmt = '''\
<first variable> <second one>
<next line thing>
'''

filename = None
with NamedTemporaryFile(mode='w', delete=False) as f:
    filename = f.name

data = {
    'first variable': 123,
    'second one': 555,
    'next line thing': 908
}

fvar.dump(fmt, data, filename)

with open(filename, 'r') as f:
    print('dump:')
    print(f.read(), end='')

os.unlink(filename)

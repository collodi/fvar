from context import fvar

import os
from tempfile import NamedTemporaryFile

fmt = '''\
<first variable> <second one>
# don't do anything for this line
# <variable?>
<next line thing>
'''

text = '''\
12 515 1
53
'''

filename = None
with NamedTemporaryFile(mode='w', delete=False) as f:
    filename = f.name
    f.write(text)

obj = fvar.parse(fmt, filename)
print(obj)

os.unlink(filename)

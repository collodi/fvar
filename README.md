# fvar
Python package for importing/exporting variable-formatted files

## Usage

```python
# input.txt
2 5
7

# parse_example.py
import fvar

fmtstr = '''\
# this line will be ignored
<x> <y>
<z>'''

data = fvar.parse(fmtstr, 'input.txt')
print(data) # { 'x': 2, 'y': 5, 'z': 7 }
```

```python
# dump_example.py
import fvar

fmtstr = '''\
<a> <b>
<c>'''

data = { 'a': 5, 'b': 7, 'c': 4 }
fvar.dump(fmtstr, data, 'output.txt')

# output.txt
5 7
4
```

To comment, the line must start with `#`. Inline comments are not supported.

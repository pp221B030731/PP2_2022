import re

with open("row.txt", 'r') as f:
	t = f.read()
l = ''.join(x.capitalize() or '_' for x in t.split('_'))
print(l)
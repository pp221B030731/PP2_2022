import re

with open('row.txt') as f:
	t = f.read()
l = re.findall(r"\S*a.*б\b|\S*a.*b\b", t)
print(l)
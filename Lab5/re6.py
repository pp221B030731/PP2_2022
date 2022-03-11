import re

with open("row.txt", 'r') as f:
	t = f.read()
l = re.sub("[ .,]", "|", t)
print(l)
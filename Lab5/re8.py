import re

with open("row.txt", 'r') as f:
	t = f.read()
l = re.split('[A-Z]|[А-Я]', t)
print(*l)
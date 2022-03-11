import re

with open("row.txt", 'r') as f:
	t = f.read()
l = re.sub('([A-Z][a-z]*)([A-Z][a-z]*)|([А-Я][а-я]*)([А-Я][а-я]*)', r"\1 \2", t)
print(l)
import re

with open("row.txt", 'r') as f:
	t = f.read()
l = re.findall("[A-Z]+[a-z]+|[А-Я]+[а-я]+", t)
print(l)
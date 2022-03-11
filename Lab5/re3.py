import re

#with open("row.txt", 'r') as f:
#	t = f.read()
t = input()
l = re.findall("[a-z]+_[a-z]+|[а-я]+_[а-я]+", t)
print(l)
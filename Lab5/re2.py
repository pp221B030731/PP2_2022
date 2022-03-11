import re

with open("row.txt", 'r') as f:
	t = f.read()
l = re.findall("\S*ab{2, 3}\S*|\S*аб{2, 3}\S*", t)
print(l)
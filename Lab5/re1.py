import re

with open("row.txt", 'r') as f:
	t = f.read()
l = re.findall("\S*ab*\S*|\S*аб*\S*", t)
print(l)
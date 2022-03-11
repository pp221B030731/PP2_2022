import re

with open("row.txt", 'r') as f:
	t = f.read()
li = re.findall("[A-Z]\w*[A-Z]\w*|[А-Я]\w*[А-Я]\w*", t)
ans = ''
for x in re.split(' |\n', t):
	if x in li:
		if re.search('([A-Z]\w*)([A-Z]\w*)', x):
			ans += re.sub("([A-Z]\w*)([A-Z]\w*)", r'\1_\2 ', x).lower()
		else:
			ans += re.sub("([А-Я]\w*)([А-Я]\w*)", r'\1_\2 ', x).lower()
	else:
		ans += x + ' '
print(ans)
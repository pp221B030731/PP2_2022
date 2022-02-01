s = str(input())
a = 0
l = len(s)-1
for i in s:
	if i == '1':
		a += 2**l
	l -= 1
print(a)
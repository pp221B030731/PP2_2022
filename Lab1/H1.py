s = str(input())
t = str(input())
a = 0
x1 = y1 = 0
j = 0
for i in s:
	if i == t:
		if a == 0:
			x1 = j
		else:
			y1 = j
		a += 1
	j += 1
if a == 1:
	print(x1)
else:
	print(x1, y1)
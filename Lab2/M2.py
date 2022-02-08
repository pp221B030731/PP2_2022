def f(s):										# key function for sort
	a, b, c = s.split()
	g = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #list of days in each m
	m = 0
	for i in range(int(b)-1):
		m += g[i]
	return int(a) + m + int(c)*365

l = []
a = str(input())
while a != '0':
	l.append(a)
	a = str(input())
l.sort(key = f)
for i in l:
	print(i)
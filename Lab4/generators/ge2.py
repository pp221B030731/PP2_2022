def gen(n):
	x = 0
	while x <= n:
		yield x
		x += 2

n = int(input())
a = gen(n)
for i in a:
	print(i, end = ', ')
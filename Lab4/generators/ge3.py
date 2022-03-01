def gen(n):
	x = 12
	while x <= n:
		yield x 
		x += 12

n = int(input())
a = gen(n)
for i in a:
	print(i, end = ', ')
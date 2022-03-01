def squ(n):
	x = 0
	while x*x <= n:
		yield x*x
		x += 1

n = int(input())
a = squ(n)
def gen(n):
	while n >= 0:
		yield n
		n -= 1

n = int(input())
a = gen(n)
for i in a:
	print(i)
def squares(a, b):
	for i in range(a, b+1):
		yield i*i

a, b = map(int, input().split())
s = squares(a, b)
for i in s:
	print(i)
import random
l = [random.randint(1, 100) for i in range(random.randint(2, 100))]
m = max(l)
print(l)
for i in range(2, int(m**0.5)+2):
	l = list(filter(lambda a: a != 1 and (a < i*i or a%i), l))
for i in l:
	print(i, end = ' ')
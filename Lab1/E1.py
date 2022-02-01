def p(a):
	i = 2
	if a > 499:
		return False
	while i*i <= a:
		if a%i == 0:
			return False
		i += 1
	return True

d, c = input().split()
d = int(d)
c = int(c)
if p(d) and c%2 == 0:
	print("Good job!")
else:
	print("Try next time!")


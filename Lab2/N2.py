l = []
a = int(input())
while a != 0:
	l.append(a)
	a = int(input())
le = len(l)
for i in range(le//2):
	print(l[i] + l[le-1-i], end = ' ')
if le % 2 == 1:
	print(l[le//2])
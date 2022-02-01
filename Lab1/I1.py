n = int(input())
l = []
for i in range(n):
	a = str(input())
	h = a.find("@gmail.com")
	if h != -1:
		l.append(a[:h])
for i in l:
	print(i)
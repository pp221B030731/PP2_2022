n = 0
a = int(input())
b = str(input())
if b == "b":
	print(a * 1024)
else:
	g = a/1024
	n = int(input())
	print(round(g, n))
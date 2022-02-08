px, py = map(int, input().split())
n = int(input())
l_p = {}
for i in range(n):
	x, y = map(int, input().split())
	d = (px-x)**2 + (py-y)**2  #distance to P
	if d in l_p:
		d += x*0.01
	l_p[d] = "{} {}".format(x, y)	#d is a key in dic while "x, y" is item
for i in sorted(l_p):				#sorting by distance 
	print(l_p[i])

	#"l"
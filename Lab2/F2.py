n = int(input())
d = {}
for i in range(n):
	a, b = input().split()
	if a in d: 
		d[a] += int(b)
	else:
		d[a] = int(b)
max = 0
for i in d:			# finding max value to compare with other
	if max < d[i]:
		max = d[i]
for i in sorted(d): # to output in sorted way
	if d[i] == max:
		print(i, "is lucky!")
	else:
		print(i , "has to receive {} tenge".format(max - d[i]))

		# ("H"  
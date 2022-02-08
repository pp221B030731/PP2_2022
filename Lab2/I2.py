n = int(input())
l = []
a = []
for i in range(n):
	s = input()
	if len(s) > 1:
		l.append(s[2:])
	else:
		a.append(l[0]) #add to list of taken out
		l.pop(0)		# pop from first list
for i in a:
	print(i, end = ' ')
#"l"
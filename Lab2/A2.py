a = list(map(int, input().split())) #for place numbers from str to list
j = 1
f = True
for i in a[:(-1)]: # checkin last element is not neadable
	#If list has break point "0"
	if i == 0:
		b = 0
		for k in a[:(j-1)]:
			if k + b >= j: #if there way from break point
				f = False
				break
			b += 1
		if f:
			print(0)
			quit()
		f = True
	j += 1
	#-------------------------

print(1) #if still working than there no break points

d1 = {}	
n = int(input())
for i in range(n):			#making dic with weakneses as key and number of them as items
	a, b = input().split()
	if b in d1:
		d1[b] += 1
	else:
		d1[b] = 1
n = int(input())
for i in range(n):  		#if there key in dic then minus till 0
	a, b, c = input().split()
	if b in d1:
		if d1[b] <= int(c):
			d1[b] = 0
		elif d1[b] > int(c):
			d1[b] -= int(c)
sum = 0
for i in d1:				# finding left demons
	sum += d1[i]
print("Demons left:", sum)
# "e"
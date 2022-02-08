n = int(input())
max1 = max2 = 0 #because min a[i] is 1 
a = list(map(int, input().split()))
for i in a:
	if max1 <= i:
		max2 = max1
		max1 = i 	#finding 2 maximum
	elif max2 < i:
		max2 = i    #if max1 > i but max2 < i
print(max1*max2)
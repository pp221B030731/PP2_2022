s = set(map(str, input().split()))
lis = []
for i in s:
	l = ''
	for j in i:
		if "A" <= j and j <= "Z" or j >= "a" and j <= "z":
			l += j
	lis.append(l) #list with unique words without Punctuation marks
lis.sort() #sort lexicographically
print(len(lis))
for i in lis:
	print(i)
# " "
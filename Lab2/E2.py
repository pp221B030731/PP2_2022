s = input()
i = s.find(' ')
if i > 0:		# checking if input in one line
	n = int(s[:i])
	x = int(s[i:])
else:
	n = int(s)
	x = int(input())
a = x
for i in range(1, n):
	a = a^(x+2*i)	#finding xor between last and new elements, no need for list
print(a)
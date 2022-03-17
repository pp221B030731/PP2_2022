s = input()

i = j = 0

for k in s:
	if k.isupper():
		i += 1
	elif k.islower():
		j += 1
print(i, j)
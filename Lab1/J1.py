s = str(input())
j = ""
l = s.split(" ")
for i in l:
	if len(i) >= 3:
		j += i + " "
print(j)
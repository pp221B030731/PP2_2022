def toLowercase(a):
	g = ""
	for i in a:
		if i >= 'A' and i <= 'Z':
			g += chr(ord(i)+32)
		else:
			g += i
	return g
		
s = str(input())
print(toLowercase(s))
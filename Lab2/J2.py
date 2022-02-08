n = int(input())
l = set()	#set to have only unique
for i in range(n):
	u = False
	lo = False	#falgs for upercase, lowercase, number
	nu = False
	a = input()
#	if a in l:
#		continue
	for i in a:
		if 'A' <= i and i <= 'Z':	
			u = True
		elif 'a' <= i and i <= 'z':
			lo = True
		elif '0' <= i and i <= '9':
			nu = True
	if nu and u and lo:	#if str have all 3 flags it is strong
		l.add(a)
print(len(l))
for i in sorted(l):
	print(i)
	#"p"
def f(s):
	rev = ''
	l = list(s.split())
	for i in range(len(l)-1, -1, -1):
		rev += l[i] + ' '
	return s + ' -> ' + rev

s = input()
print(f(s))
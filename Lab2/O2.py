l = ['ZER','ONE', 'TWO', 'THR', 'FOU', 'FIV', 'SIX', 'SEV', 'EIG', 'NIN']

def to_N(s):	#to make numbers using list l 
	n = ''
	b = 0
	for i in range(0, len(s), 3):
		a = s[i] + s[i+1] + s[i+2]
		for j in range(10):
			if l[j] == a:
				b = j
		n += str(b)
	return n

def to_S(n):	#to print answer using list l
	for i in str(n):
		print(l[int(i)], end = '')

m1, m2 = input().split('+') 
to_S(int(to_N(m1)) + int(to_N(m2)))
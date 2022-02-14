from itertools import permutations

def f(s):
	return permutations(s)

s = input()
for i in f(s):
	ans = ''
	for j in i:
		ans += j
	print(ans)
	
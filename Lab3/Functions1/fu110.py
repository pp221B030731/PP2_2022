def f(l):
	ans = []
	for i in l:
		if i not in ans:
			ans.append(i)
	return ans
	
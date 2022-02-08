a = input()
l = []
bi = ['(', '{', '[']
bo = [')', '}', ']'] #list of bracers to make it a litl easy

for i in a:
	if i in bo:
		if len(l) == 0: #if bo bracers first than No
			print('No')
			quit()
		else:
			if l[-1] == '[' and i == ']' or l[-1] == '{' and i == '}' or l[-1] == '(' and i == ')':
				l.pop()	#pop last element in list
			else:
				print('No')
				quit()
	else:
		l.append(i)

if len(l) == 0: #if smt left then No
	print('Yes')
else:
	print('No')

n = int(input())
l = []
for i in range(n):
	a = int(input())
	l.append(a)
for i in l:
	if i <= 10:
		print("Go to work!")
	elif i <= 25:
		print("You are weak")
	elif i <= 45:
		print("Okay, fine")
	else:
		print("Burn! Burn! Burn Young!")
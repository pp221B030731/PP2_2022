n = int(input())
if n%2 == 0:	#if even
	for i in range(n):
		print(('#'*(i+1))+('.'*(n-i-1)))
else:			#if odd
	for i in range(n):
		print(('.'*(n-i-1))+('#'*(i+1))) # "." n-1-i times "#" i+1 times
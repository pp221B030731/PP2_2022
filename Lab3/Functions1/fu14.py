def filter_prime(l):
	primes = []
	for i in l:
		if i != 0 and i != 1:
			p = True
			for j in range(2, int(i**0.5)+2):
				if i % j == 0:
					p = False
			if p:
				primes.append(i)
	return primes

l = map(int, input().split())
print(filter_prime(l))
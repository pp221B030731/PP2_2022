from random import randint

c = 1
name = input('Hello! What is your name?\n')
print("\nWell, {}, I am thinking of a number between 1 and 20.".format(name), "\nTake a guess.")
ans = randint(1, 20)
n = int(input())
while n != ans:
	if n < ans:
		print("\nYour guess is too low.\nTake a guess.")
	else:
		print("\nYour guess is too high.\nTake a guess.")
	n = int(input())
	c += 1
print(f"\nGood job, {name}! You guessed my number in {c} guesses!")

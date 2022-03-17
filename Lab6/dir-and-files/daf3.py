import os

p = input()

if os.path.exists(p):
	print("True")
	print(os.path.basename(p))
	print(os.path.dirname(p))
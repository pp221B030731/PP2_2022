import os

p = input()

if os.path.exists(p):
	print(os.access(p, os.F_OK), os.access(p, os.R_OK), os.access(p, os.W_OK), os.access(p, os.X_OK))
	os.remove(p)
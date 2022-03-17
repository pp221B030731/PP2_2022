import os

p = input()

def only_dir(p):
	l = []
	for i in os.listdir(p):
		if os.path.isdir(os.path.join(p, i)):
			l.append(i)
	return 

def only_file(p):
	l = []
	for i in os.listdir(p):
		if os.path.isfile(os.path.join(p, i)):
			l.append(i)
	return l

def both(p):
	return os.listdir(p)

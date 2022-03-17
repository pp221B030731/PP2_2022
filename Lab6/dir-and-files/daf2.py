import os

p = input()

f = os.access(p, os.F_OK)
r = os.access(p, os.R_OK)
w = os.access(p, os.W_OK)
x = os.access(p, os.X_OK)
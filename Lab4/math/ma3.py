import math

n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))
print("The area of the polygon is:", int((n/4) * (a**2) * (1/math.tan(math.radians(180/n)))))
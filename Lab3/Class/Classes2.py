class Shape:
	s = 0
	def area(self):
		print(self.s)

class Square(Shape):
	def __init__(self, l):
		self.s = l**2

n = int(input()) #Length of square
a = Square(n)
a.area()
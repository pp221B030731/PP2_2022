class Shape:
	s = 0
	def area(self):
		print(self.s)

class Rectangle(Shape): 
	def f(self, l, w):
		self.s = l*w

	def __init__(self, l, w):
		self.f(l, w)


l, w = map(int, input().split()) # Length and Width
r = Rectangle(l, w)
r.area()
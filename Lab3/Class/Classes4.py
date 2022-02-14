class Point:
	x = y = 0
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def show(self):
		print(self.x, self.y)

	def move(self, x, y):
		self.x += x
		self.y += y

	def dist(self, a):	# a in another point or object of class Point
		return ((self.x - a.x)**2 + (self.y - a.y)**2)**0.5

p1 = Point(2, 2)
p2 = Point(0, 0)
p1.show()
p2.move(1, 1)
print(p1.dist(p2))	#prints 1,41... dist from 1, 1 to 2, 2 

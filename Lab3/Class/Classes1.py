class SomeClass:
	s = ''
	def getString(self):
		self.s = input()
	
	def printString(self):
		print(self.s.upper())

a = SomeClass()
a.getString()
a.printString()
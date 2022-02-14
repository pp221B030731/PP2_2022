class Account:
	owner = ''
	balance = 0

	def __init__(self, a):	#when creating account in bank, balance is 0
		self.owner = a

	def deposit(self, s):
		self.balance += s

	def withdraw(self, s):
		if s > self.balance:
			print("Sorry, not enough funds")
		else:
			self.balance -= s

	def __str__(self):
		return self.owner, self.balance

	def sb(self):
		if self.balance == 1:
			print("You balance is", self.balance, "NuraliCoin")
		elif self.balance == 0:
			print("You do not have any funds")
		else:
			print("You balance is", self.balance, "NuraliCoins")

a1 = Account("Nurali")
a1.deposit(10)
a1.deposit(2)
a1.sb()
a1.withdraw(13)
a1.withdraw(11)
a1.sb()
class Dog: 
	kind = 'canine'
	tricks = []

	def __init__(self, name):
		self.name = name

	def add_trick(self, trick):
		self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print d.kind
print e.kind
print d.name
print e.name
d.add_trick('roll over')
d.add_trick('play dead')
print d.tricks
print e.tricks

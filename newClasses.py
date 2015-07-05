class MyClass: 
	variable = "blah"

	def function(self): 
		print "Message withing a class"

myObject = MyClass()

myObject.variable

print myObject.variable

myObjecty = MyClass()
myObjecty.variable = "yip"

print myObject.variable
print myObjecty.variable

myObject.function()


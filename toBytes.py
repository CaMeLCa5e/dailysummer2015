m = memoryview('abc')
print m.tobytes()

class C: 
	def method(self):
		pass 
c = C()
# c.method.whoami = "method"

c.method.im_func.whoami = 'my name is method'
print c.method.whoami
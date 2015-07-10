if __name__ == '__main__':
	def myFunc(s):
		words = s.split(" ")
		return len(words)

	sc = SparkContext(...)
	sc.textFile("file.txt").map(myFunc)

# class MyClass(object): 
# 	def func(self, s):
# 		return s 
# 	def doStuff(self, rdd): 
# 		return rdd.map(self.func)

class MyClass(object):
	def __init__(self):
		self.field = "Hello"
		def doStuff(self, rdd):
			return rdd.map(lambda s: self.field + s)

def doStuff(self, rdd): 
	field = self.field
	return rdd.map(lambda s: field + s)
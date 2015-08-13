def fib(n): 
	a,b = 1, 1
	for i in range(n-1): 
		a,b = b, a+b
	return a 
print fib(15)


def fibR (n):
	if n == 1 or n == 2:
		return 1
	return fib(n-1)+fib(n-2)					
print fibR(5)

# generator fib 
a,b = 0,1
def fibI():
	global a,b
	while True: 
		a, b = b, a+b 
		yield a
f = fibI()
f.next()
f.next()
f.next()
f.next()
f.next()
f.next()
f.next()
f.next()
f.next()
f.next()
f.next()
f.next()
print f.next()

def memoize(fn, arg): 
	memo = {}
	if arg not in memo: 
		memo[arg] = fn(arg)
		return memo[arg]

fibm = memoize(fib, 85)

print fibm


# fib decorators 
class Memoize:
	def __init__(self, fn):
		self.fn = fn
		self.memo = {}
	def __call__(self, arg):
		if arg not in self.memo: 
			self.memo[arg] = self.fn(arg)
			return self.memo[arg]
@Memoize 
def fib(n): 
	a, b = 1, 1
	for i in range(n-1): 
		a,b = b, a+b 
	return a 
print fib(25)		
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



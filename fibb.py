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

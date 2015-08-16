!# usr/bin/env python

def factorial(n):
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result")
        return res
print (factorial(5))


def iterative_factorial(n):
    result = 1
    for i in range(2, n+1):
        result * = i
    return result

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibi(n):
    old, new = 0, 1
    if n == 1:
        return 0
    for i in range (n-1):
        old, new = new, old + new
    return new

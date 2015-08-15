!# usr/bin/env python

def factorial(n):
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result")
        return res
print (factorial(5))

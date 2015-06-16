def f(x): return x % 3 == 0 or x % 5 == 0 

print filter(f, range(2, 25))

def cube(x): return x*x*x
print map(cube, range(1, 11))

seq = range(8)
def add(x, y): return x+y 

print map(add, seq, seq)
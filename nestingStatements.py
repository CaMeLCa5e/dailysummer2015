t = 12345, 54321, 'hello'
t = [0]

print t 

u = t, (1,2,3,4,5)
print u 

t[0] = 99999
print t

v = ([1, 2+3 ,3], [4,3,2])
print v 
# Did you see how mutable that object is?! 
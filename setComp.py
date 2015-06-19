a = {x for x in 'lmno' if x not in 'abc'}
print a


# iterates through word removing all the a characters
b = {x for x in 'abracadabra' if x not in 'a'}  

print b
print type(b)
print len(b)


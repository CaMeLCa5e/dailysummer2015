dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.viewkeys()
print keys
values = dishes.viewvalues()
print values

n = 0 
for val in values:
	n += val 
print(n)

print list(keys)
print list(values)

del dishes['eggs']
del dishes['sausage']
print list(keys)

print keys & {'eggs', 'bacon', 'salad'}

print keys 
print values

print {'a', 'b', 'c'}
print keys & {'eggs', 'bacon', 'salad'}
print keys & {'eggs', 'bacon', 'salad'}
x = {'t', 'L', 'm'}
print x & {'t', 'L', 'salad'}
print x - {'t', 'L'}
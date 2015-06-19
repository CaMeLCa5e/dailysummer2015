basket = ['apple', 'orange', 'apple', 'pear', 'bananna']
fruit = set(basket)
print fruit

print 'orange' in fruit
print 'grass' in fruit

a = set('abracadabra')
b = set('alacazam')

print a - b
print a | b # either or
print a & b 
print a ^ b # letters in a or b but not both. 


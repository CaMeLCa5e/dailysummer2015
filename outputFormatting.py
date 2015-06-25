for x in range(1, 11):
        print (repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
        print (repr(x*x*x).rjust(4))

for y in range(1, 11):
print ('{0:2d}{1:3d}{2:4d}'.format(x, x*x, x*x*x)

table = {'Bill': 4322, 'Jack':9908, 'piggy': 2232342}
for name, phone in table.items():
        print ('{0:10}')==> '{1:10d}'.format(name, phone))

f = open('workfile', 'w')
f.read()

for line in f: 
        print (line, end='')

f.write('This is a test\n')

value = ('The answer, 42)
s = str(value)
f.write(s) 
	

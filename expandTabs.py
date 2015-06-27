import re 

print '01\t12\t\123\t0123456'.expandtabs(1)
print '01\t12\t\123\t0123456'.expandtabs(4)

if 'Py' in 'Python':
	print True

print "sum of 1 + 2 is {0}".format(1+2)

print '    spacestrip     '.lstrip()

print 'www.example.com'.lstrip('cmow.')

x = 'ABCDEFGHIJKLMNOPQRSTUVWQYS'

print x.partition('HI')
print x.replace('HI', 'lmno')
print x.rfind('HI', 1 )
print x.rindex('QY', 1)
print x.rjust(40, '0')
print x.rsplit('ST')
print 'ABCDEFGH I   JKLMNOPQRSTUVWQYS'.rstrip('S') 
#only removes trailing chars
print 'mississippi'.rstrip('ipz')
print x.splitlines()

def titlecase(s):
	return re.sub(r"[A-Za-z]+(['A-Za-z']+)?",
					lambda mo: mo.group(0)[0].upper()+
							   mo.group(0)[1:].lower(), s)

print titlecase("they're bill's friends.")
print "they're bill's friends.".title()	
# ".translate(None, 'aeiou')


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
	print "-- This parrot wouldn't", action,
	print "if you put", voltage, "volts through it"
	print "Lovely plumage the", type
	print "-- It's", state, "!"

parrot(1000)
parrot(voltage=1000)
parrot(voltage=100000, action='MOOO')
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the dasies')
parrot(1, 1, 1, 1)
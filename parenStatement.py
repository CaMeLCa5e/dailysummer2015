vec = [-4, -2, 0, 2, 4]
print [x*2 for x in vec]

print [x for x in vec if x >= 0]
print [abs(x) for x in vec]

freshfruit = ['bananna', '   berry', 'passionfruit   ']
[weapon.strip() for weapon in freshfruit]

print [(x, x**2) for x in range(6)]

[x, x**2 for x in range(6)]
	file "<stdin>", line 1
		print [x, x**2 for x in range(7)] # this err is expected. 


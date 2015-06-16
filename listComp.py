squares = []
for x in range(10): 
	squares.append(x**2)

print squares

squares2 = [x**2 for x in range(10)]

print squares2

print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y: 
			combs.append((x, y))

print combs
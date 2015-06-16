def cheeseshop(kind, *arguments, **keywords):
	print "-- Do you have any", kind, "?"
	print "-- I'm sorry, were all out of", kind
	for arg in arguments: 
		print arg
	print "-" * 40 
	keys = sorted(keywords.keys())
	for kw in keys:
		print kw, ":", keywords[kw]



print "1"
cheeseshop("Swiss", "It's very runny, sir.",
			"it's really very, very runny.",
			shopkeeper="Mike",
			client="John",
			sketch="cheese shop sketch")

print "2"
cheeseshop("It's very runny, sir.",
			"it's really very, very runny.",
			shopkeeper="Mike",
			client="John",
			sketch="cheese shop sketch")
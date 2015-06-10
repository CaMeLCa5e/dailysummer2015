loop = 1

choice = 0

while loop == 1: 
	print "Calculator"
	print " "

	print "1) +"
	print "2) -"
	print "3) *"
	print "4) /"
	print "5) quit"
	print " "

	choice = input("choose an option")
	if choice == 1: 
		add1 = input("Add this: ")
		add2 = input("to this: ")
		print add1, "+", add2, "=", add1 + add2
	elif choice == 2:
		sub2 = input("subtract this: ")
		sub1 = input("from this: ")
		print sub1, "-", sub2, "=", sub1 - sub2
	elif choice == 3: 
		mull = input("Multiply this: ")
		mull2 = input("with this: ")
		print mull, "*", mull2, '=', mull * mull2 
	elif choice == 4: 
		div1 = input("Divide this: ")
		div2 = input("by this: ")
		print div1, '/', div2, '=', div1 / div2
	elif choice == 5: 
		loop = 0 


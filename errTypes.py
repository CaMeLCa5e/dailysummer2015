while True:
	try: 
		x = int(input("Please enter a number"))
		break 
	except ValueError:
		print("...Try again, that was not a number...")
class Dogs: 
	ears = "2 ears"
	legs =  "4 legs"

	def sound(self):
		print "Woof"

boxer = Dogs()

print boxer.legs
print boxer.ears


boxer.tail = "wiggily"
print boxer.tail

print boxer.sound()

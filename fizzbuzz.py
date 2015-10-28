running = True

while running:
	print("1. Start")
	print("2. Beenden")
	cmd = int(input("Hier Zahl eingeben:"))
	if cmd == 1:
		for i in range(1,101):
			if i % 15 == 0:
				print "FizzBuzz"
			elif i % 3 == 0:
				print "Fizz"
			elif i % 5 == 0:
				print "Buzz"
			print i
	if cmd == 2:
		print("Beenden")
		running = False
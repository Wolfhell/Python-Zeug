running = True

while running:
	print("1.test")
	print("2.Beenden")
	command = int(input("Hier Zahl eingeben:"))
	if command == 1:
		text = raw_input("Hier Text eingeben:")
		print text[::-1]
	else:
		print("Beenden")
		running = False
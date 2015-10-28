running = True

vokale = "aeiou"

while running:
	print("1.test")
	print("2.Beenden")
	command = int(input("Hier Zahl eingeben:"))
	if command == 1:
		text = raw_input("Hier Text eingeben:")
		text = text.lower()
		for vokal in vokale:
			print vokal, text.count(vokal)
	if command == 2:
		print("Beenden")
		running = False
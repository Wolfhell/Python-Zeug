running = True

while running:
	print("1. Berechnen")
	print("2. Beenden")
	cmd = int(input("Hier Zahl eintragen:"))
	if cmd == 1:
		print("Steuerberechnung")
		kosten = int(input("Hier die Kosten eintrage:"))
		steuer = int(input("Hier die Steuer eintragen:"))
		prozent = steuer/100
		steuer1 = kosten*prozent
		ergebnis = kosten+steuer1
		print("Die Summe der Steuer betraegt ",steuer1," und die Gesamtsumme betraegt",ergebnis)
	if cmd == 2:
		print("Beenden")
		running = False
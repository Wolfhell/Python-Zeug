running = True

while running:
	print("1 = Addition")
	print("2 = Subtraktion")
	print("3 = Multiplikation")
	print("4 = Division")
	print("5 = Potenz berechnen")
	print("6 = Beenden")
	cmd = int(input("Nummer eingeben: "))
	#Berechnet Plus
	if cmd == 1:
		print("Addition")
		first = int(input("Hier erste Zahl eingeben:"))
		second = int(input("Hier zweite Zahl eingeben:"))
		result = first + second
		print(first,"+",second,"=",result)
	#Berechnet Minus
	elif cmd == 2:
		print("Subtraktion")
		first = int(input("Hier erste Zahl eingeben:"))
		second = int(input("Hier zweite Zahl eingeben:"))
		result = first - second
		print(first,"-",second,"=",result)
	#Berechnet Mal
	elif cmd == 3:
		print("Multiplikation")
		first = int(input("Hier erste Zahl eingeben:"))
		second = int(input("Hier zweite Zahl eingeben:"))
		result = first * second
		print(first,"*",second,"=",result)
	#Berechnet Geteilt
	elif cmd == 4:
		print("Division")
		first = int(input("Hier erste Zahl eingeben:"))
		second = int(input("Hier zweite Zahl eingeben:"))
		result = first / second
		print(first,"/",second,"=",result)
	#Berechnet die Potenz
	elif cmd == 5:
		first = int(input("Hier erste Zahl eingeben:"))
		second = int(input("Hier zweite Zahl eingeben:"))
		result = first ** second
		print("Die Potenz von",first,"^",second,"ist", result)
	#Beendet das Script
	elif cmd == 6:
		print("Beenden")
		running = False
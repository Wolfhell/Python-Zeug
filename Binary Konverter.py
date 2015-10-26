running = True

while running:
    print("1. Konvertierung zu Dezimal")
    print("2. Konvertierung zu Binary")
    print("3. Beenden")
    cmd = int(input("Nummer eingeben: "))
    if cmd == 1:
        print("Konvertierung zu Dezimal")
        erst = input("Hier Binaryzahl eingeben:")
        zwei = str(erst)
        ergebnis = int(zwei, 2)
        print("Die konvertierte Zahl ist: ",ergebnis)
    elif cmd == 2:
        print("Konvertierung zu Binary")
        erst = int(input("Hier Nummer eingeben:"))
        ergebnis = bin(erst)
        print("Die konvertierte Zahl ist: ",ergebnis)
    elif cmd == 3:
        print("Beenden")
        running = False
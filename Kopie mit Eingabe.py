import os
import sys
import shutil

source = raw_input("Hier Pfad der Quelldatei eingeben:")
dest = raw_input("Hier Pfad des Ziels eingeben:")

if not os.path.isfile(source):
	print "Quelldatei %s existiert nicht." % source
	sys.exit(3)
	
try:
	shutil.copy2(source, dest)
except IOError, e:
	print "Konnte die Datei %s nicht zum Ziel %s kopieren" % (source, dest)
	print e
	sys.exit(3)
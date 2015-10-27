import os
import glob

os.chdir("c:\\users\\praktikant\\desktop\\test123")

files = glob.glob("test*.jpg")
for file in files:
	parts = file.split("-")
	new_name = "zeug -{}".format(parts[1])
	os.rename(file, new_name)
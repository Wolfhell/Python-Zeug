import os
import glob
files = glob.glob('test*.jpg')
for file in files:
    os.rename(file, 'zeug -{}'.format(file.split('-')[1]))
import os
import shutil

def copyFile(src, dst):
    try:
        shutil.copy2(src, dst)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)
		
copyFile("C:\\neu.txt", "C:\\test")
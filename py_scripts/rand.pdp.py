from random import randrange
import os

path = r'D:/pdp/'
path2 = r'D:/pdp/terraria/'
pathTop = r'D:/Top/'

files = os.listdir(path)
files2 = os.listdir(path2)
filesTop = os.listdir(pathTop)

for f in filesTop:
    if not f.endswith('.mp4'):
        filesTop.remove(f)

for f in files:
    if not f.endswith('.mp4'):
        files.remove(f)


filesN = len(files)
files2N = len(files2)
filesTopN = len(filesTop)

def openFile():
    b = randrange(0, 2)
    if (b == 0):
        a = randrange(0, filesN)
        print("selected ", files[a])
        os.startfile(path + files[a])
    elif (b != 0):
        a = randrange(0, files2N)
        print("selected ", files2[a])
        os.startfile(path2 + files2[a])

def openFileTop():
    a = randrange(0, filesTopN)
    print("selected ", filesTop[a])
    os.startfile(pathTop + filesTop[a])

openFile()

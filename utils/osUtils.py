import os
import tarfile
import glob


def getfileoftype(dir, type):
    files=[]
    for x in os.walk(dir):
        for y in glob.glob(os.path.join(x[0], '*.%s' % type)):
            files.append(y)
    return files

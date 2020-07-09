import osUtils
import time
from playsound import playsound

dir = 'C:\Users\Administrator\Desktop\data'

for i in osUtils.getfileoftype(dir,'wav'):
    print i
    mp3 = playsound(i)
    time.sleep(5)

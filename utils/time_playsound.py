import time
from datetime import datetime
from playsound import playsound



clocktime = datetime(2020,7,9,17,58)
while datetime.now() < clocktime:
    print "it's not yet" ,clocktime
    time.sleep(5)

else:
    mp3 = playsound('C:/Users/Administrator/Desktop/data/test.wav')
    time.sleep(5)

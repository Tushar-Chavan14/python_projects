import pywhatkit as kit
import datetime as dt

hour = dt.datetime.now()
minute = dt.datetime.now()
print(hour,minute)

def senmsg(number,message):
    kit.sendwhatmsg(number,message,12,50)
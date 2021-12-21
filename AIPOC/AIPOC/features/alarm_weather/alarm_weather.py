from time import sleep
import datetime
from PIL import Image, ImageTk
from playsound import playsound
from main_program import speak

def set_alarm(query):
    file1 = open("alarm.txt","r+")
    file1.truncate(0)
    file1.close()
    with open('alarm.txt','w') as fb:
        fb.write(query)




def alarm():
    with open('alarm.txt','r') as fb:
        timetable=fb.readline()
    print(timetable)
    while(True):
        hour = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        str_ = str(hour)+":"+str(min)
        print(str_)
        if str_==timetable:
            playsound('1.mp3')
            sleep(0.5)
            playsound('1.mp3')
            sleep(0.5)
            playsound('1.mp3')
            sleep(0.5)
            playsound('1.mp3')
            speak('get up master')
            sleep(0.5)
            playsound('1.mp3')
            sleep(120)
        sleep(30)
set_alarm("11:6")
alarm()
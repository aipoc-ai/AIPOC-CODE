from main_program import speak
from datetime import datetime

def tell_time():
    current_datetime = datetime.now()
    hour_hand = str(current_datetime.hour)       
    minute_hand = str(current_datetime.minute)   
    time = hour_hand+":"+minute_hand
    d = datetime.strptime(time, "%H:%M")
    time_12_hours = d.strftime("%I:%M %p")
    speak("Now the time is"+time_12_hours)

tell_time()
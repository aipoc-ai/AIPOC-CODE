import smtplib, ssl
from main_program import speak,command

def mail():
    speak("Whom do you want to mail?")
    while True:
        receiver_name = command()
        speak("you said"+receiver_name+"."+"is it ok")
        permission = command()
        if "yes" in permission:
            break
        else:
            speak("say again receiver name")
    while True:
        speak("what is the message")
        message = command()
        speak("i am repeating the message."+message+"Is it ok?")
        permission = command()
        if "yes" in permission:
            break
        else:
            speak("say again receiver name") 

    sender_mail = "rootaccess369@gmail.com"
    passw = "****"   
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(sender_mail, passw) 
    s.sendmail(sender_mail,receiver_name, message) 
    s.quit() 
    speak("mail sended")
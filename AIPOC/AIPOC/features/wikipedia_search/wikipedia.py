from main_program import speak
import wikipedia

def wikipedia_command(query):
    speak("searching in wikipedia, Sir")
    print("searching...")
    query = query.replace("wikipedia","")
    result = wikipedia.summary(query, sentences= 2)
    print("According to wikipedia",end=" ")
    print(result)
    speak("According to wikipedia")
    speak(result)
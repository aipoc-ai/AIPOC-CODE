from distutils.command.upload import upload
from speaker.speaker import command,speak2,speak
from play_music.play_audio import play_music_func
from time import sleep
import signal
import os
from ques_ans.ques_ans import get_ans
from get_weather.get_weather import get_weather
from remove_stopwords.remove_stop_words import remove_words
from basic_ques.basic_question import name_owner
# from send_mail import mail
from wake_word.porcupine_demo_mic import PorcupineDemo
import pvporcupine
from capture_photos.capture_photo import capture
from capture_video.capture_video import  capturevideo
from face_Detection_py.facefrontend import capture_face
from colour_Detect.colours import colors
while True:
    try:
        keyword = ['jarvis',"bumblebee"]
        keyword_paths = [pvporcupine.KEYWORD_PATHS[x] for x in keyword]
        sensitivities = [0.5] * len(keyword_paths)
        PorcupineDemo(
            library_path=pvporcupine.LIBRARY_PATH,
            model_path=pvporcupine.MODEL_PATH,
            keyword_paths=keyword_paths,
            sensitivities=sensitivities,
            output_path=None,
            input_device_index=-1).run()
        speak("     Yes    sir?")
        x = command()
        x = x.lower()
        #play music
        if ("play music" in x) or ("play song" in x):
            speak("please tell me song?")
            query = command()
            t = play_music_func(query)
        elif "play" in x:
            music = list(x.split(' '))
            music.remove("play")
            t = play_music_func(" ".join(music))

        
        #get ans
        elif list(x.split(' '))[0] in ['what','who','tell','whose']:
            if ("weather" in x) or ("temperature" in x):
                try:
                    city_name = remove_words(x)
                    temperature,list_ = get_weather(str(city_name))
                    speak("the temperature of "+str(city_name)+ "is "+str(temperature)+" at "+str(list_[0])+" and the weather is "+str(list_[1])+".")
                except:
                    speak("i don't understand the name of the city please ask again?")
            elif ("my name" in x) or ("your owner" in x):
                x = name_owner()
                speak(x)
            else:
                speak(get_ans(x))

        elif "wait" in x: 
            speak("ok sir?")
            sleep(60)


        elif "Take my pictures" in x or "take picture" in x or "click photos" in x or "open camera" in x:
            print("Taking picture")

            capture()
            #upload to google drive
            speak("Picture is uploaded to google drive")

            
        elif "recognise me" in x:
            print("recognise")
            speak(capture_face())
        elif "detect colour" in x:
            print("detecting")
            colors()
            
        elif "take video" in x:
            speak("capturing video")
            capturevideo()
            speak("video captured")

        elif x in "exit":
            break
        elif x in "exit":
            break
        elif x in "exit":
            break
        elif x in "exit":
            break
        elif x in "exit":
            break
        elif x in "exit":
            break
        elif x in "exit":
            break
        elif x in "exit":
            break
        elif ("stop music" in x) or ("stop song" in x):
            try:
                print(t)
                os.killpg(os.getpgid(t), signal.SIGTERM)
            except:
                speak("no music is playing. I can play music for you only you have to say play music aipoc")
        
        else:
            speak("I am learning this right now?")

    except Exception as e:
        print(e)
        # speak("hello i am aipoc")
        # speak("there is no internet connection please connect me?")
        break
from speaker.speaker import command,speak2,speak
from play_music.play_audio import play_music_func
from time import sleep
import signal
import os
# from ques_ans import get_ans
# from get_weather import get_weather
from remove_stopwords.remove_stop_words import remove_words
from basic_ques.basic_question import name_owner
# from send_mail import mail
from wake_word.porcupine_demo_mic import PorcupineDemo
import pvporcupine
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
        speak2("     Yes    sir?")
        x = command()
        x = x.lower()
        #play music
        if ("play music" in x) or ("play song" in x):
            speak2("please tell me song?")
            query = command()
            t = play_music_func(query)
        elif "play" in x:
            music = list(x.split(' '))
            music.remove("play")
            t = play_music_func(" ".join(music))

        
        #get ans
        # elif list(x.split(' '))[0] in ['what','who','tell','whose']:
        #     if ("weather" in x) or ("temperature" in x):
        #         try:
        #             city_name = remove_words(x)
        #             temperature,list_ = get_weather(str(city_name))
        #             speak2("the temperature of "+str(city_name)+ "is "+str(temperature)+" at "+str(list_[0])+" and the weather is "+str(list_[1])+".")
        #         except:
        #             speak2("i don't understand the name of the city please ask again?")
        #     elif ("my name" in x) or ("your ownwer" in x):
        #         x = name_owner()
        #         speak2(x)
        #     else:
        #         speak2(get_ans(x))

        elif "wait" in x: 
            speak2("ok sir?")
            sleep(60)

        # elif "send mail" in x:
        #     mail()

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
                speak2("no music is playing. I can play music for you only you have to say play music aipoc")
        
        else:
            speak2("I am learning this right now?")

    except Exception as e:
        print(e)
        # speak2("hello i am aipoc")
        # speak2("there is no internet connection please connect me?")
        break
import features.hot_word_detection.hot_word_detection as wake_word
import features.speaker.speaker as speaker
import features.get_weather.get_weather as weather
import features.ques_ans.ques_ans as give_ans
import features.basic_ques.basic_question as info
import features.remove_stopwords.remove_stop_words as words
import features.play_music.play_audio as play_song

class AIPOCAI:
    def __init__(self):
        pass

    def hot_word_detect(self, lang='en'):
        try:
            status, command = wake_word.hot_word_detection(lang=lang)
            print(status, command)
        except Exception as e:
            status = command = False
        return status, command

    def mic_input(self, lang='en'):
        pass

while(True):
    Ai = AIPOCAI()
    status,command = Ai.hot_word_detect()
    if status:
        if len(list(command.split(" ")))<2:
            speaker.speak("Yes sir")
            query = speaker.command()

        else:
            query = command
        
        if list(query.split(' '))[0] in ['what','who','tell','whose']:
            if ("weather" in query) or ("temperature" in query):

                city_name = words.remove_words(query)
                temperature,list_ = weather.get_weather(str(city_name))
                speaker.speak("the temperature of "+str(city_name)+ "is "+str(temperature)+" at "+str(list_[0])+" and the weather is "+str(list_[1])+".")

            elif ("my name" in query) or ("your ownwer" in query):
                x = info.name_owner()
                speaker.speak(x)
            else:
                speaker.speak(give_ans.get_ans(query))

        if ("play music" in query) or ("play song" in query):
            speaker.speak("please tell me song?")
            query = speaker.command()
            t = play_song.play_music_func(query)
        elif "play" in query:
            music = list(query.split(' '))
            music.remove("play")
            t = play_song.play_music_func(" ".join(music))
        elif ("stop music" in query) or ("stop song" in query):
            try:
                t.kill()
            except:
                speaker.speak("no music is playing. I can play music for you only you have to say play music aipoc")

        


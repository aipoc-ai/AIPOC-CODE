from gtts import gTTS
import speech_recognition as sr
import os
from time import sleep
import pygame
import pyttsx3
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def watsonspeak(text):
    authenticator = IAMAuthenticator('_ICF9BgFjuLYx6GSx7luNeeVUYy2ChzF65lNiHdT_1cK')
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/6382eb61-3ceb-4c38-9eb0-d6c898b87a20')

    with open('hello_.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                text,
                voice='en-US_MichaelV3Voice',
                accept='audio/wav'        
            ).get_result().content)
    pygame.mixer.init()
    pygame.mixer.music.load("hello_.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def speak(text):
    txt = gTTS(text = text)
    file_name = "voice.mp3"
    txt.save(file_name)

    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


def speak2(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(text)
    engine.runAndWait()

def command():
    while True:
        try:
            r1 =sr.Recognizer()
            with sr.Microphone() as source:
                print("Listning...")
                r1.pause_threshold = .8
                r1.energy_threshold = 8000
                audio = r1.listen(source)
            print("Recognizing...")
            query = r1.recognize_google(audio, language ='en-in')
            print("user said:",query)
            break
        except:
            speak("sorry sir ,i dont understand that can you speak it again")
    return query



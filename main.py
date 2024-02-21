import speech_recognition as sr
import pyttsx3 as p
from selenium_web import *
from yt_auto import *

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',140)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def speak(command):
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()

speak("hello sir , i am your voice assiatant")
speak("How are you?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    command = r.recognize_google(audio)
    print(command)
if "what" and "about" and "you" in command:
    speak("i am also having a good day sir")
    speak("what can I do for you??") 

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    command2 = r.recognize_google(audio)
    print(command2)



if "information" in command2:
    speak("sure sir,you need information about which topic?")

    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor) 

elif "play" and "video" or "play" and "music" or "youtube" in command:
    speak("you want me to play which video??")
    
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    speak("playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)



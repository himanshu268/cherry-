import urllib.request
import re
from datetime import datetime
from win32com.client import Dispatch
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greed():
    time_hour = datetime.now().hour
    if(time_hour<12):
        greed="Good Morning"
        return greed
    elif(12<=time_hour<16):
        greed="Good Afternoon"
        return greed
    else:
        greed="Good evening"
        return greed
speak(greed()+" cherry")
speak("myself jadoo How can i help you sir!!")

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=0.5
        r.energy_threshold=250
        audio=r.listen(source)

    try:
        inuser=r.recognize_google(audio,language="en-in") #covert into words
        print("User said: " + inuser)
    except Exception as e:
        b="please say again!!"
        print(b)
        return "None"
    return inuser
        # speak.Speak(b)
if __name__ == "__main__":
    greed()
    t=1
    while True:
        t-=1
        search_keyword=listen().lower()
        if 'wikipedia' in search_keyword:
            print("searching ....")
            search_keyword=search_keyword.replace('wikipedia','')
            result= wikipedia.summary(search_keyword,sentences=2)
            print(result)
            speak('According to wikipidea')
            speak(result)
        elif 'play' in search_keyword:
            print("searching ....")
            search_keyword='makhna'
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"https://i.ytimg.com/vi/(\S{11})", html.read().decode())
            tab="https://www.youtube.com/watch?v=" + video_ids[0] 
            webbrowser.open(tab)
        elif 'play music' in search_keyword:
            webbrowser.open('https://www.youtube.com/watch?v=rrBE8ZuAtgY&list=RDrrBE8ZuAtgY&start_radio=1')
        elif 'open google' in search_keyword:
            webbrowser.open('google.com')  
        elif 'stop' in search_keyword:
            speak('thank you')
            exit()
        

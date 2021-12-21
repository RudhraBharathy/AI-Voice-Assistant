import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import webbrowser
import pyjokes
import randfacts
import os
import psutil
import wikipedia
import pyautogui
import requests
import json
import weathercom
from wikisel import *
from selyt import *
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
repeat=0
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.8
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")

        except Exception as e:
            print("I am sorry,please repeat it")
            return "None"
        return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")


def weatherreport(city):
    weatherdetails = weathercom.getCityWeatherDetails(city)
    temp = json.loads(weatherdetails)["vt1observation"]["temperature"]
    humid = json.loads(weatherdetails)["vt1observation"]["humidity"]
    phrase = json.loads(weatherdetails)["vt1observation"]["phrase"]
    return temp, humid, phrase


if __name__ == '__main__':
    wishMe()
    speak("I am Your personal assistant, how are you")
    print("I am Your personal assistant, how are you")
    while True:
        text = takecommand().lower()

        if "What" and "about" in text and "yourself" in text:
           speak("I am good,what can i do for you!")
           print("I am good,what can i do for you!")

        elif 'date' in text:
            curDate = datetime.datetime.now().strftime("%d:%B:%Y")
            curDay = datetime.datetime.now().strftime("%A")
            print(f"Today's date is {curDate} and the day {curDay}")
            speak(f"Today's date is {curDate} and the day {curDay}")
        elif 'time' in text:
            curTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Now the Time is {curTime} ")
            speak(f"Now the Time is {curTime} ")
        elif "open" and "browser" in text:
            speak("Opening your Browser")
            webbrowser.open(url="https://duckduckgo.com")
        elif 'open' and 'linkedin' in text:
            speak('Opening LinkedIn in Webrowser')
            webbrowser.open(url="https://linkedin.com")
        elif 'open' and 'S N S' and 'College' and 'website' in text:
            speak('Opening S N S college of Technology in Webrowser')
            webbrowser.open(url="https://main.snsct.org")
        elif "open" in text and "Github":
            speak("Opening github in your Browser")
            webbrowser.open(url="https://github.com")
        elif "open" in text and "YouTube":
            speak("Opening youtube in your Browser")
            webbrowser.open(url="https://youtube.com")


        elif"joke" in text:
            Joke = pyjokes.get_joke('en','neutral')
            print(Joke)
            speak(Joke)

        elif "facts" in text:
            Fact = randfacts.getFact()
            print(Fact)
            speak(Fact)

        elif "open" in text and "code" in text:
            speak("opening visual studio code")
            codePath = "D:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "cpu stats" in text:
            usage = str(psutil.cpu_percent())
            speak('cpi is at' + usage)

            battery = psutil.sensors_battery()
            speak("battery is at")
            speak(battery.percent)

        elif "according to wikipedia" in text:
            speak("searcing in wikipedia...")
            word =text.replace("wikipedia","")
            results = wikipedia.summary(word,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "take" in text and "screenshot" in text:
            img = pyautogui.screenshot()
            speak("Done sir,I am saving it.")
            img.save(f"E:\\Mini Project\\screenshot\\img{repeat}.png")
            repeat+=1

        elif "take notes" in text:
            speak("what should i write sir?")
            notes = takecommand()
            file = open(f"E:\\Mini Project\\Notes\\notes{repeat}.txt",'w')
            repeat+=1
            speak("should i include date and time ?")
            if "yes" or "sure" in text:
                curTime = datetime.datetime.now().strftime("%H:%M:%S")
                curDate = datetime.datetime.now().strftime("%d:%B:%Y")
                file.write(curTime)
                file.write(curDate)
                file.write(':-')
                file.write(notes)
                speak("Done taking notes sir")

            else:
                file.write(notes)
                speak("Done taking notes sir")

        elif "show notes" in text:
            speak("opening notes")
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif "news" in text:
            api_address =  "https://newsapi.org/v2/top-headlines?country=in&apiKey=3c5b2cc319c74916990c5ad5923054ab"

            response = requests.get(api_address)
            news_json = json.loads(response.text)

            count = 3

            print("Here are today's Top headlines")
            speak("Here are today's Top headlines")
            for news in news_json['articles']:
                if count>0:
                    T = str(news['title'])
                    print(T)
                    speak(T)
                    count -= 1

        elif "weather" in text:
            print("Sure ,Please name me the city")
            speak("Sure ,Please name me the city")
            city = takecommand()
            humid , temp , phrase = weatherreport(city)
            print("Currently in "+city+ " the Temperature is "+str(temp)+" degree celcius ,with humidity of "+ str(humid) + "percent and sky is "+phrase)
            speak("Today's weather report : Currently in "+city+ "the Temperature is "+str(temp)+" degree celcius ,with humidity of "+ str(humid) + "percent and sky is "+phrase)

        elif "information" in text:
            speak("please name the topic")
            topic = takecommand()
            print("Searching {} in wikipedia".format(topic))
            speak("Searching {} in wikipedia".format(topic))
            assist = info()
            assist.getinfo(topic)
        elif "play" in text and "online" in text:
            speak("what do you want me to play")
            title = takecommand()
            print("Playing {} in youtube".format(title))
            speak("Playing {} in youtube".format(title))
            bot = music()
            bot.play(title)
        elif "go offline" in text:
            speak("Iam going offline")
            print("Going Offline...😀")
            quit()




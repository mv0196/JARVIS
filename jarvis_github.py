import pyttsx3
import os
import wikipedia
import smtplib
import speech_recognition as sr
import webbrowser
import datetime
import random
import sys
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[0].id)


chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning sir!')

    elif hour >=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("I am Jarvis . How may i help you?")

def takeCommand():
    #it take voice input and return string,if it is unable to recogninse it will return a string "None"
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        #r.energy_threshold = 400
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(f"User said:{query}")

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtplib.gmail.com",587)
    server.elho()
    server.starttle()
    server.login("Your email id","Your password")
    server.sendmail("Your email id",to,content)
    server.close()

if __name__=="__main__":
    speak("Welcome!")

    wishme()
    while True:
        #query=takeCommand().lower()
        query="go to"

        #logics for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open google and search" in query or "search" in query:
            q=query.split(" ")
            s=" ".join(q[q.index("search")+1:])
            speak("Opening Google")
            webbrowser.get(using='chrome').open("http://google.com/search?q="+s)

        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.get(using='chrome').open("youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.get(using='chrome').open("google.com")

        elif "open facebook" in query or "open fb" in query:
            speak("Opening facebook")
            webbrowser.get(using='chrome').open("facebook.com")

        elif "open stack over flow" in query or "open stack overflow" in query:
            speak("Opening Stackoverflow")
            webbrowser.get(using='chrome').open("stackoverflow.com")

        elif "open gmail" in query or "open mail" in query or "open my gmail" in query or "open my mail" in query or"open email" in query or "open my email" in query:
            speak("Opening Your Gmail sir")
            webbrowser.get(using='chrome').open("gmail.com")

        elif "open insta" in query or "open instagram" in query:
            speak("Opening Your instagram account sir")
            webbrowser.get(using='chrome').open("instagram.com")

        elif "open whatsapp" in query:
            speak("Opening whatsapp")
            webbrowser.get(using='chrome').open("web.whatsapp.com")


        elif "play" in query and "music" in query:
            music_dir="path to music directory"
            songs=os.listdir(path=music_dir)
            s=random.randint(1,len(songs)-1)
            while songs[s][-3:]!='mp3':
                s=random.randint(1,len(songs))
            os.startfile(os.path.join(music_dir,songs[s]))
            time.sleep(7)

        elif "open atom" in query:
            codePath="C:\\Users\\HP\\AppData\\Local\\atom\\atom.exe"
            os.startfile(codePath)
            speak("Opening atom")

        elif "email to" in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                sendEmail("email id of reciever",content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry can't send email!")

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "day today" in query or "date today" in query:
            n=datetime.datetime.today().weekday()
            if n==0:
                speak("Today is Monday sir")
            elif n==1:
                speak("Today is Tuesday sir")
            elif n==2:
                speak("Today is Wednesday sir")
            elif n==3:
                speak("Today is Thrusday sir")
            elif n==4:
                speak("Today is Friday sir")
            elif n==5:
                speak("Today is Saturday sir")
            elif n==6:
                speak("Today is Sunday sir")

        elif "ml folder" in query and "machine learning folder" in query:
            speak("Opening Machine Learning folder sir!")
            os.startfile("D:\\ML_Python")

        elif "explorer" in query:
            speak("Opening main explorer sir!")
            os.system('explorer')

        #elif "navigate to ml folder and open jupyter notebook" in query:
        #    speak("Opening Jupyter notebook sir!")


        elif "open cmd" in query or "open command prompt" in query:
            codePath="C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(codePath)
            speak("Opening Command prompt")

        elif "open cmd here" in query or "open command prompt here" in query:
            os.system("start cmd")
            speak("Opening Command prompt")

        elif "date" in query:
            d=str(datetime.date.today()).split("-")
            d=" ".join(d[::-1])
            speak(d)


        elif "wait for " in query:
            n="".join([i for i in query if i in "1234567890"])
            speak("I will be back soon sir!")
            try:
                time.sleep(int(n))
            except:
                time.sleep(10)
            speak("I am back sir!")


        elif "wait" in query:
            speak("I will be back to service in 7 seconds!")
            time.sleep(7)
            speak("I am back sir!")

        elif "quit" in query:
            speak("Bbye,See you soon sir")
            sys.exit()

        else:
            speak("Say again !")

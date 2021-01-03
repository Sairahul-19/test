#project
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your Intelligent Charlie, Please tell me how may i help you")

def takeCommand():
    #microphone input and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you ......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Sorry , i didnt get you, Can you say that again please")
        print("Sorry , i didnt get you, Can you say that again please")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('hemanthmodani2001@gmail.com','****')
    server.sendmail('hemanthmodani2001@gmail.com',to,content)
    server.close()

if _name_ == "_main_":
    wishMe()
    while True:
       query=takeCommand().lower()
       #logics begins here
       if 'wikipedia' in query:
           speak("Searching Wikipedia....")
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           speak(results)
           print(results)
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'open google' in query:
           webbrowser.open("google.com")
       elif 'play music' in query:
           music_dir='C:\\Users\\Hemanth modani\\fav music'
           songs=os.listdir(music_dir)
           os.startfile(os.path.join(music_dir, songs[0]))
       elif 'the time' in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir , the time is {strTime}")
       elif 'who created you' in query:
           speak('Rollnos 10 31 33 35 63 65 of B5 section created me')
       elif 'email to 63' in query:
           try:
             speak("What should i say?")
             content=takeCommand()
             to="121910305063@gmail.com"
             sendEmail(to,content)
             speak('email has been sent')
           except Exception as e:
               print(e)
               speak('sorry email is not sent')
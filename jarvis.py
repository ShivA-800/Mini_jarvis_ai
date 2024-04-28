import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine=pyttsx3.init()

#creating a function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#time function
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

#date function
def date():
    #Date=datetime.datetime.now().strftime("%d-%m-%y")
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    present_date=int(datetime.datetime.now().day)
    speak("the current date is")
    speak(present_date)
    speak(month)
    speak(year)
   

#wishing greeting
def wish():
    speak("Welcome Back Boss!")
    time()
    date()
    hr=datetime.datetime.now().hour
    if hr >= 6 and hr<12:
        speak("Good Morning Boss!")
    elif hr >=12 and hr<18:
        speak("Good afternoon Boss!")
    elif hr>=18 and hr<24:
        speak("Good Evening Boss!")
    else:
        speak("Good night")  

    speak("Iam listening.Jarvis is on duty Boss.")

def open_brave():
    os.system("start brave")

def search(query):
    search_url = f"https://www.google.com/search?q={query}"
    os.system(f"start brave {search_url}")

def play_songs():
    songs_dir = 'C:/Users/Radharapu Shiva/Music'
    songs = [file for file in os.listdir(songs_dir) if file.endswith(('.mp3', '.wav', '.ogg'))]
    if len(songs) == 0:
        speak("No songs found in the directory")
        return
    first_song = os.path.join(songs_dir, songs[0])
    os.system(f'start wmplayer "{first_song}"')

# def screenshot():
#     img=pyautogui.screenshot()
#     img.save() path to save the file

def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery=str(psutil.sensors_battery())
    speak("battery is at" + battery)
    print(battery)

def jokes():
    a=speak(pyjokes.get_joke())
    print(a)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        audio=r.listen(source,timeout=5)
    
    try:
        print("Recongnizing...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again,Didn't Recoginzed")
        return "None"
    return query

if __name__ == "__main__":
    wish()
    while True:
        query=takeCommand().lower()
        if 'open brave' in query:
            speak("Opening Brave browser")
            open_brave()
        elif 'search' in query:
            search_query = query.replace('search', '').strip()
            speak(f"Searching for {search_query}")
            search(search_query)

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'search in Brave' in query:
            speak("What should i Search?")
            bravepath='C:/Users/Radharapu Shiva/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe %s'
            search=takeCommmand().lower
            wb.get(bravepath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            play_songs()
        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot Done Boss")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()
          

        elif 'offline' in query:
            quit()


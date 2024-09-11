import smtplib
import psutil
import pyautogui
import pyjokes
import pyttsx3
import datetime
import wikipedia as wiki
from googlesearch import search
import webbrowser
import speech_recognition as sr
from pyNewsApi import PYNEWS

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    x = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The time is")
    speak(x)

def date():
    day = str(datetime.datetime.now().day)
    month = str(datetime.datetime.now().month)
    year = str(datetime.datetime.now().year)
    speak("Today's date is")
    speak(day)
    speak(month)
    speak(year)


def greet():
    hour = datetime.datetime.now().hour
    if hour >=12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good Evening")
    else:
        speak("Good Morning")

def hear():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(sourse)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)

    except:
        print("i didn't get that...")
        return "None"
    return query

def email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('','')
    server.sendmail('', to, content)
    server.close()

def screenshot():
    ss = pyautogui.screenshot()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU percentage is"+ usage)

def batteryy():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    p = "Plugged In" if plugged else ""
    speak("Your mac is at"+ str(battery.percent) + p)

def jokes():
    speak(pyjokes.get_joke())

def news():
    p = PYNEWS()
    y = p.get_headlines_by_country('in')
    print(y)

if __name__ == '__main__':
    greet()
    speak("Jarvis at your service. What can I do for you?")
    while True:
        query = hear().lower()

        if 'time' in query:
            time()

        elif "hello" in query:
            speak("Hey Ghee!")
        elif "hey" in query:
            speak("Hey! Nice to see you again.")

        elif 'date' in query:
            date()
        elif 'thank' in query:
            speak("It's my pleasure. Anything else I can help you with?")

        elif 'remember' in query:
            speak("What do you want me to remember?")
            data = hear()
            speak("You said me to remember that"+ data)
            x = hear()
            if "y" in x:
                remember = open('data.txt', 'a')
                remember.write('\n' + str(data))
                remember.close()
                speak("Done")

            if "no" in x:
                speak("Sorry. Can you repeat that?")

        elif "do i have any reminder" in query:
            remember = open('data.txt', 'r')
            speak("Yes. You have these reminders{0}".format(remember.readlines()))
            remember.close()

        elif 'screenshot' in query:
            screenshot()
            speak("Done")

        elif 'search in chrome' in query:
            speak("What do you want me to search?")
            chrome_path = '/Applications/Safari.app'
            search = hear().lower()
            webbrowser.get(chrome_path).open_new_tab(search)

        elif 'google' in query:
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)

        elif 'wikipedia'in query:
            speak("Searching for it")
            query = query.replace("wikipedia","")
            search = wiki.summary(query, sentences=3)
            print(search)
            speak(search)

        elif 'who is' in query:
            query = query.replace("who is","")
            search = wiki.summary(query, sentences=3)
            print(search)
            speak(search)

        elif 'battery' in query:
            batteryy()
        elif 'CPU' in query:
            cpu()

        elif "joke" in query:
            jokes()

        elif "tell me today's news" in query:
            news()


        elif 'mail'in query:
            try:
                speak("Whom do you want to send?")
                to = hear()
                speak("What do you want me to say?")
                content = ''
                email(to, content)
                speak("The e-mail was sent.")
            except:
                print("error")
                speak("The mail couldn't be sent.")

        elif 'bye' in query:
            speak("until we talk again")
            quit()

        else:
            speak("I didn't get that. Could you try again?")

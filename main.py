import pyttsx3  # text to speech
import datetime
import speech_recognition as sr
import random
import wikipedia
import webbrowser
import os
from datetime import date
import videoTester
engine = pyttsx3.init('sapi5')  # sapi5 = speech API, ,helps in recognition
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # to make the speech audible


def wish():
    hour = int(datetime.datetime.now().hour)  # will give the current hour 1-24
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak(" How may I assist you?")


def takeAudio():
    r = sr.Recognizer()  # initialising the recogniser
    with sr.Microphone() as source:  # using mic as source
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1  # it will start recognising if no voice input is given for 1 sec
        audio = r.listen(source)

    try:  # if no error in recognising
        print("recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")
    except Exception as e:  # if error occurs, it will print line 44
        print("Pardon me, please say that again")
        return "None"
    return query


def wakeWord(audio):
    WAKE_WORDS = ['hey cookie', 'hello cookie']
    audio = audio.lower()
    for phrase in WAKE_WORDS:
        if phrase in audio:
            return True
    return False


def greeting(audio):
    # Greeting Inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'wassup', 'hello']

    # Greeting Response back to the user
    GREETING_RESPONSES = ['whats good', 'hello',
                          'hey there', 'hi', 'hey', 'hola']

    for word in audio.split():  # removing the silence in audio input
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'
    return ''


def assistantResponse(audio):
    print(audio)
    # Convert the text to speech
    speak(audio)


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


if __name__ == "__main__":
    if videoTester.live() != 1:
        exit()
    audio = takeAudio()
    response = ''
    if (wakeWord(audio) == True):
        # Check for greetings by the user
        response = response + greeting(audio)
        assistantResponse(response)

    wish()
    while True:

        # Checking for the wake word/phrase
        query = takeAudio().lower()

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open vs code' in query:
            path = "C:\\Users\\Khushi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Khushi\\Music'
            songs = os.listdir(music_dir)
            s = random.choice(songs)
            os.startfile(os.path.join(music_dir, s))

        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {Time}")

        elif 'the date' in query:
            date = datetime.date.today()
            today = date.today()
            wd = today.weekday()
            days = ["monday", "tuesday", "wednesday",
                    "thursday", "friday", "saturday", "sunday"]
            speak(f"It's {days[wd]}, the {date}")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'battery' in query:
            cpu()

        elif 'thank you' in query:
            speak('you are welcome!')
            break

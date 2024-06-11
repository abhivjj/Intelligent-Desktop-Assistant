import time
from smtplib import SMTP
import pyjokes
import pyautogui
import pyttsx3
import speech_recognition
import os
import pywhatkit
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def formalities():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning,Sir")
    elif 12 < hour <= 18:
        speak("Good Afternoon,Sir")

    else:
        speak("Good Evening,Sir")

    speak("Please tell me, How can I help you ?")


def email():
    smtp_server = "smtp.gmail.com"
    port = 587

    email_id = "avijayvargia07@gmail.com"
    password = "bnvh whep owxz earl"

    user_email = input(speak("Tell me the mail id"))

    server = SMTP(smtp_server, port)
    server.starttls()
    server.login(email_id, password)

    subject = input(speak("Tell me the subject"))
    body = input(speak("Tell me the message"))
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(email_id, user_email, msg)
    server.quit()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Pls say that again please")
        return "None"
    return query


if __name__ == "__main__":
    formalities()

    while True:
        query = takeCommand().lower()
        if " hello matrix" in query:
            speak("Hey sir, how are you")

        elif "who are you" in query:
            speak("I am your personal AI assistant")

        elif 'how are you' in query:
            speak("Perfect Sir, Thank you for asking")

        elif 'who created you' in query:
            speak("That i cannot tell you sir as i have been warned against it by my creator!")

        elif 'what is' in query:
            speak("Searching wikipedia...")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'who is' in query:
            speak("Searching wikipedia...")
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "open google" in query:
            speak("What do you want to know")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=3)
            speak(results)

        elif "open youtube" in query:
            speak("What do you want to watch")
            qry = takeCommand().lower()
            pywhatkit.playonyt(f"{qry}")

        elif "search on youtube" in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif "close browser" in query:
            os.system("taskkill /f /im chrome.exe")

        elif "what is the current time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif "type" in query:
            query = query.replace("type", "")
            pyautogui.typewrite(f"{query}", 0.1)

        elif "open chrome" in query:
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

        elif "open downloads" in query:

            pyautogui.hotkey("ctrl", "j")

        elif "maximise this window" in query:
            pyautogui.hotkey("alt", "space")
            time.sleep(1)
            pyautogui.press("x")

        elif "open new window" in query:
            pyautogui.hotkey("ctrl", "n")

        elif " joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "open" in query:
            from APP import openapp

            openapp(query)

        elif "close" in query:
            from APP import closeapp

            closeapp(query)

        elif "email" in query:
            email()

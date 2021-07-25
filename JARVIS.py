import pyautogui
from datetime import date, datetime
import datetime
import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import wikipedia
from wikipedia.wikipedia import languages
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction
from englisttohindi.englisttohindi import EngtoHindi


Assistant = pyttsx3.init()
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate',190)


def speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    Assistant.runAndWait()


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

    try:
        print("Recognizing...")
        query = command.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")

    except Exception as Error:
        speak("Say That Again Please...")
        return "none"
    return query.lower()


def Taskexe():

    def time():
        time = datetime.datetime.now().strftime("%I:%M:%S")
        speak("The Current Time is :")
        speak(time)

    def date():
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        speak("The Current Date is :")
        speak(f"{date} : {month} : {year}")

    def Music():
        speak("Tell Me the NAme of the song")
        Musicname = takecommand()

        if 'evolution' in Musicname:
            os.startfile('C:\\Users\\Ayan\\Desktop\\YouTube Project\\MUSIC\\evolution.mp3')

        else:
            pywhatkit.playonyt(Musicname)
       
    def whatsapp():
        speak("Tell Me the Name of the Person")
        name = takecommand()

        if 'Ayan' in name:
            speak("Tell me the Message")
            msg  =takecommand()
            speak("Tell me the TIme Sir")
            speak("Time in Hour")
            hour = int(takecommand())
            speak("Time in minuteutes")
            minute = int(takecommand())
            pywhatkit.sendwhatmsg("+91----------", msg, hour, minute,)
            speak("Ok Sir, Sending Whatsapp Message!")

        elif 'amma' in name:
            speak("Tell me the Message")
            msg  =takecommand()
            speak("Tell me the TIme Sir")
            speak("Time in Hour")
            hour = int(takecommand())
            speak("Time in Minutes")
            minute = int(takecommand())
            pywhatkit.sendwhatmsg("+91------------", msg, hour, minute)
            speak("Ok Sir, Sending Whatsapp Message!")

        elif 'atir bro' in name:
            speak("Tell me the Message")
            msg  =takecommand()
            speak("Tell me the TIme Sir")
            speak("Time in Hour")
            hour = int(takecommand())
            speak("Time in Minutes")
            minute = int(takecommand())
            pywhatkit.sendwhatmsg("+91------------", msg, hour, minute)
            speak("Ok Sir, Sending Whatsapp Message!")

        else:
            speak("Tell me the phone Number")
            phone = int(takecommand())
            ph = "'+91' + phone"
            speak("Tell me the message sir")
            msg  =takecommand()
            speak("Tell me the TIme Sir")
            speak("Time in Hour")
            hour = int(takecommand())
            speak("Time in minuteutes")
            minute = int(takecommand())
            pywhatkit.sendwhatmsg(ph, msg, hour, minute, 10)
            speak("Ok Sir, Sending Whatsapp Message!")  

    def openapps():
        speak("Ok Sir, wait a second ")

        if 'code editor' in query:
            os.startfile('C:\\Users\\Ayan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

        elif 'chrome' in query:
            os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

        elif 'firefox' in query:
            os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

        elif 'audacity' in query:
            os.startfile('C:\\Program Files (x86)\\Audacity\\audacity.exe')

        elif 'edge' in query:
            os.startfile('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
            
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'linkedin' in query:
            webbrowser.open('https://www.linkedin.com/feed/')

        elif 'open youtube channel' in query:
            webbrowser.open('https://www.youtube.com/channel/UCp6cRwQhZ6HL7W8pJVW1y0w')
        
        elif 'creator studio' in query:
            webbrowser.open('https://studio.youtube.com/channel/UCp6cRwQhZ6HL7W8pJVW1y0w/analytics/tab-overview/period-default')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/place/Afzal+Ahmad/@25.4216116,81.8156119,17z/data=!4m5!3m4!1s0x398535447d61a825:0x26d2a7cbe52e8e56!8m2!3d25.4216821!4d81.8188457')
        
        speak("your Command has been successfully completed")

    def closeapps():
        speak('Ok Sir, Wait A second')

        if 'chrome' in query:
            os.system('TASKKILL /F /im chrome.exe')

        elif 'code editor' in query:
            os.system('TASKKILL /F /im Code.exe')

        elif 'firefox' in query:
            os.system('TASKKILL /F /im firefox.exe')

        elif 'edge' in query:
            os.system('TASKKILL /F /im msedge.exe')

        elif 'audacity' in query:
            os.system('TASKKILL /F /im audacity.exe')

        elif 'youtube' in query:
            os.system('TASKKILL /F /im chrome.exe')

        elif 'instagram' in query:
            os.system('TASKKILL /F /im chrome.exe')

        elif 'facebook' in query:
            os.system('TASKKILL /F /im chrome.exe')

        elif 'youtube channel' in query:
            os.system('TASKKILL /F /im chrome.exe')

        elif 'linkedin' in query:
            os.system('TASKKILL /F /im chrome.exe')

        elif 'creator studio' in query:
            os.system('TASKKILL /F /im chrome.exe')

        elif 'maps' in query:
            os.system('TASKKILL /F /im chrome.exe')      

    def youtubeauto():
        speak("Whats Your Command")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'file mode' in comm:
            keyboard.press('t')

        speak("Done Sir")
        
    def chromeauto():
        speak("Chrome Automation Started")
        command = takecommand()
        
        if 'close this tab' in command:
            keyboard.press('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press('ctrl + t')

        elif 'open new window' in command:
            keyboard.press('ctrl + n')

        elif 'oepn history' in command:
            keyboard.press('ctrl + h')

        elif 'open download' in command:
            keyboard.press('ctrl + d')

        speak("Done Sir")

    def dict():
        speak("Activated Dictionary")
        speak("Tell me the Word Sir")
        word = takecommand()

        if 'meaning' in word:
            word = word.replace("What is the","")
            word = word.replace("jarvis","")
            word = word.replace("of","")
            word = word.replace("meaning","")
            word = word.replace("meaning of","")
            result = Diction.meaning(word)
            speak(f"The Meaning of {word} is {result}")

        elif 'synonym' in word:
            word = word.replace("What is the ","")
            word = word.replace("jarvis ","")
            word = word.replace("of ","")
            word = word.replace("synonym ","")
            word = word.replace("synonym of ","")
            result = Diction.synonym(word)
            speak(f"The synonym of {word} is {result}")

        elif 'antonym' in word:
            word = word.replace("What is the ","")
            word = word.replace("jarvis ","")
            word = word.replace("of ","")
            word = word.replace("antonym ","")
            word = word.replace("antonym of ","")
            result = Diction.antonym(word)
            speak(f"The Antonym of {word} is {result}")

        speak("Exited Dictionary!")

    def trans():
        speak("Activated Translation")
        speak("Tell Me the Words Sir")
        word = takecommand()

        if 'translation' in word:
            word = word.replace("What is the ","")
            word = word.replace("jarvis ","")
            word = word.replace("of ","")
            word = word.replace("translate ","")
            word = word.replace("translation ","")
            word = word.replace("translate of ","")
            word = word.replace("translation of ","")
            result = EngtoHindi(word)
            final = result.convert
            speak(f"The translation of {word} is {final}")

        else:
            speak("sorry Sir i Could not Translate it")

    def screenshot():
        speak("Ok Sir, What Should I name that file?")
        path = takecommand()
        pathname = path + ".png"
        path1 = "C:\\Users\\Ayan\\Documents\\Screenshots\\" + pathname
        ss = pyautogui.screenshot()
        ss.save(path1)
        os.startfile("C:\\Users\\Ayan\\Documents\\Screenshots")
        speak("Here is your Screenshot sir")


    while True:

        query = takecommand()

        if 'hey' in query:
            speak("Hello Sir")
            speak("How May I Help You?")

        elif 'how are you' in query:
            speak("I Am Fine Sir!")
            speak("Whats About You?")

        elif 'i am good jarvis' in query:
            speak("Thats Great Sir!")

        elif 'tell me about yourself' in query:
            speak("I Am Jarvis, Your Personal  AI Assistant")

        elif 'good morning' in query:
            speak("Good morning Sir. It's 7 A.M. The weather in Allahabdad is 33 degrees with scattered clouds. The surf conditions are fair with waist to shoulder highlines, high tide will be at 10:52 a.m.")

        elif 'you need a break' in query:
            speak("Ok Sir, You can Call me Anytime")
            break

        elif 'bye' in query:
            speak("ok sir, bye bye")
            break

        elif 'youtube search' in query:
            speak("Ok sir , This is what i found for your search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("Done Sir!")

        elif 'google search' in query:
            speak("This is what i found for your search SIR")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            speak("done sir")

        elif 'open a website' in query:
             speak("Tell me sir NAme of the website")
             name = takecommand()
             web = 'https://www.' +  name + '.com'
             webbrowser.open(web)
             speak("done Sir")

        elif 'website' in query:
            speak("Ok Sir, Launching ....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' +  web1 + '.com'
            webbrowser.open(web2)
            speak("Launched Sir")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query, sentences = 2)
            speak(f"According to wikipedia :{wiki}")

        elif 'whatsapp message' in query:
            whatsapp()
        
        elif 'screenshot' in query:
            screenshot()

        elif 'open facebook' in query:
            openapps()

        elif 'open instagram' in query:
            openapps()

        elif 'open youtube' in query:
            openapps()

        elif 'open code editor' in query:
            openapps()

        elif 'open linkedin' in query:
            openapps()

        elif 'open chrome' in query:
            openapps()

        elif 'open firefox' in query:
            openapps()

        elif 'open edge' in query:
            openapps()

        elif 'open youtube channel' in query:
            openapps()

        elif 'open creator studio' in query:
            openapps()

        elif 'open maps' in query:
            openapps()

        elif 'open audacity' in query:
            openapps()

        elif 'close chrome' in query:
            closeapps()

        elif 'close youtube channel' in query:
            closeapps()

        elif 'close creator studio' in query:
            closeapps()

        elif 'close firefox' in query:
            closeapps()
        
        elif 'close edge' in query:
            closeapps()

        elif 'close linkedin' in query:
            closeapps()

        elif 'close code editor' in query:
            closeapps()

        elif 'close facebook' in query:
            closeapps()

        elif 'close instagram' in query:
            closeapps()

        elif 'close maps' in query:
            closeapps()

        elif 'close audacity' in query:
            closeapps()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'back' in query:
            keyboard.press('j')

        elif 'file mode' in query:
            keyboard.press('t')

        elif 'youtube automation' in query:
            youtubeauto()

        elif 'close this tab' in query:
            keyboard.press('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press('ctrl + t')

        elif 'open new window' in query:
            keyboard.press('ctrl + n')

        elif 'open history' in query:
            keyboard.press('ctrl + h')

        elif 'open download' in query:
            keyboard.press('ctrl + d')

        elif 'chrome automation' in query:
            chromeauto()

        elif 'joke' in query:
            my_joke = pyjokes.get_joke(language="en", category="neutral")
            speak(my_joke)

        elif 'repeat me' in query:
            speak("Speak Sir then i will repeat you")
            repeat = takecommand()  
            speak(f"you said : {repeat}")
            
        elif 'my location' in query:
            speak("ok sir, wait a second")
            webbrowser.open('https://www.google.com/maps/@25.4218,81.8187506,19.25z')

        elif 'open dictionary' in query:
            dict()

        elif 'what is the time' in query:
            time()

        elif 'what is the date' in query:
            date()
        
        elif 'translate a sentence' in query:
            trans()

Taskexe()

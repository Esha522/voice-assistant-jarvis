import speech_recognition as sr
import webbrowser 
import pyttsx3
import music_library


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)

    else:
        # let open AI handle the request
        pass

if __name__ == "__main__":
    speak("Hey sir how are you, I am here to help you. Tell me which type of work you want me to do")


while True:
# Listen for the wake word jarvis
# obtain audio from the microphone
    r = sr.Recognizer()
    
    print("Recognizing...")

    # recognize speech using google
    try:
        with sr.Microphone() as source:
            print("Listening..")
            audio = r.listen(source, timeout=2, phrase_time_limit=1)
        
        word = r.recognize_google(audio)
        if (word.lower() == "jarvis"):
            speak("Yes, I am listening")

        #  Listen for command
        with sr.Microphone() as source:
            print("Jarvis active...")
            audio = r.listen(source)
        command = r.recognize_google(audio)
       
        processCommand(command)
   
    except Exception as e:
        print("error; {0}".format(e))
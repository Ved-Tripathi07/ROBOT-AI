import pyttsx3
import datetime
import pyaudio
import os
import wikipedia
import pytube
import webbrowser
import speech_recognition as sr


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)


''' this function is for speaking 
         what you have told to the ROBO '''

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 


''' this function wishes you and 
    introduces the AI named ROBOT '''

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(" Good Morning!Master ")
    
    elif hour>=12 and hour<18:
        speak(" Good Afternoon!Master")

    else:
        speak(" Good Evening!Master")

    speak(" I am Robot, Speed 1 terahertz, memory 1 zeta byte. ")
    speak("How may I help you ! ")
    speak("please say stop when you done your task")

''' this function takes the command from the user
     and gives the related output '''

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio= r.listen(source)
        

    try:
        print("Recoznizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"you said: {query}\n") 
    
    except Exception as e:
        print("Master Please speak again...")
        speak("Master I am sorry! I am not able to understand what you have said. Please speak again...")
        return "None"
    
    return query  



''' the main function starts 
        from here '''


if __name__=="__main__" :

    wishMe()

    
    while True:

        query = takeCommand().lower()

        if "thank you" in query:
            speak("Welcome Master ")
            speak("I will be very happy to assist you again")


            # Searching anything from wikipedia

        elif "wikipedia" in query:

            speak("Searching on Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia...")
            print(results)
            speak(results)
        

            # openning youtube

        elif "open youtube" in query:

            speak("Openning Youtube...")
            webbrowser.open("youtube.com")


        elif "open google" in query:

            speak("Openning Google...")
            webbrowser.open("google.com")


        elif "code" in query:

            speak("Openning Visual Studio Code...")
            codePath = "C:\\Users\\theve\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        # This function will give you the current time

        elif 'time' in query:

            speak("Collecting current time...")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Master, the time is {strTime}")


        elif 'stop':
            break
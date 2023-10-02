import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id) #voice property set 

# jarvis can speak with this function
def speak(audio):
       engine.say(audio) 

       engine.runAndWait()
def wishme():

 hour = int(datetime.datetime.now().hour)
 if hour>=0 and hour<12:
        speak("Good Morning!")

 elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

 else:
        speak("Good Evening!")  

 speak("I am Jarvis Sir. Please tell me how may I help you") 

def takeCommand():
    #user er kach theke input voice nei

    r = sr.Recognizer()
    with sr.Microphone() as source: #microphone command 
        print("Listening...")
        r.pause_threshold = 1 #1second er gap kotha bolar maje 
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# main method 
if __name__=="__main__" :

     speak("Welcome Back Sir ")
     wishme()
     while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) #sentence 2 is equal 2line porjonto bolbe 
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("https://web.facebook.com/masud924")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'open masudrana ' in query:
            webbrowser.open("https://masudrana-dev.vercel.app/")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
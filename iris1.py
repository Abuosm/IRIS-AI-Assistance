import pyttsx3 #this librairy convert text to speech
import speech_recognition as sr # recognizes the speech
import webbrowser # connects to the web
import pyjokes # implents the joke
import datetime #says about date n time
import time# says the time
import os

def sptxt():
    recognizer=sr.Recognizer()#object of speech recognizer
    with sr.Microphone() as source:
        print("listinig.....")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
          print("recognizing.....")
          data=recognizer.recognize_google(audio)
          print(data)
          return data
          
        except sr.UnknownValueError:
          print("does not sounds good")


def speechtxt(x):
  engine=pyttsx3.init()
  voices=engine.getProperty('voices')
  engine.setProperty('voice',voices[1].id)
  rate=engine.getProperty('rate')
  engine.setProperty('rate',150)
  engine.say(x)
  engine.runAndWait()

if __name__=='__main__':
 
  if 'iris' in sptxt().lower():
    speechtxt("myself iris,how can i help you")
    while True:

        data1=sptxt().lower()
        if "your name" in data1:
            name="my name is iris"
            speechtxt(name)

        elif 'time' in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            speechtxt(time)

        elif 'web'in data1:
            webbrowser.open(" http://www.jitd.in")     


  

        elif 'joke' in data1:
            joke1=pyjokes.get_joke(language="en",category="neutral")
            speechtxt(joke1)



        elif 'google search' in data1:
            import wikipedia as googleScrap
            speechtxt("This is what i found on the web! ")
            data1 = data1.replace("iris","")
            data1 = data1.replace("google search","")
            data1 = data1.replace("google","")
            try:
                #pywhatkit.search(data1)
                res = googleScrap.summary(data1,3)
                print(res)
                speechtxt(res)
            except:
                speechtxt("No speakable Data available")

      
        elif "see you again"in data1:
            speechtxt("thank you,it was amazing to chit chat with you,have smile")
            break

      
  else:
     print("tq")


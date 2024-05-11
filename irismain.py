import pyttsx3 #this librairy convert text to speech
import speech_recognition as sr # recognizes the speech
import webbrowser # connects to the web
import pyjokes # implents the joke
import datetime #says about date n time
import time# says the time
import pywhatkit


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
          
        except Exception as e:
            print("Can you please repeat..")
            speechtxt("Can you please repeat...")
            return "none"


def speechtxt(x):
  engine=pyttsx3.init()
  voices=engine.getProperty('voices')
  engine.setProperty('voice',voices[0].id)
  rate=engine.getProperty('rate')
  engine.setProperty('rate',150)
  engine.say(x)
  engine.runAndWait()

def wishme():
    hours = int(datetime.datetime.now().hour)
    if hours>=0 and hours<12:
        speechtxt("good Morning!")
    elif hours>=12 and hours<18:
        speechtxt("good afternoon!")
    else:
        speechtxt("Good evening!")
    speechtxt("iam iris, how can i help you")

if __name__=='__main__':

 
    if 'iris' in sptxt().lower():
        wishme()
        while True:

            data1 = sptxt().lower()
            if "your name" in data1:
                name="my name is iris"
                speechtxt(name)

            elif 'time' in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                speechtxt(time)

            elif 'website'in data1:
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
                
          
            elif 'play' in data1:   
                data1 = data1.replace("play", "")
                data1 = data1.replace("iric","")
                speechtxt("playing " + data1)
                pywhatkit.playonyt(data1)

            elif 'how are you' in data1:
                    speechtxt("I am fine, Thank you")
                    speechtxt("How are you ")
 
            elif 'fine' in data1 or "good" in data1:
                    speechtxt("It's good to know that your fine")

            elif 'principal' in data1 or 'director' in data1:
                speechtxt("principle and director of j i t is Doctor ganesh ")

            elif 'fourth sem exam' in data1:
                speechtxt("lab exam will be from 20 august and theory exams will be from third of september")

            elif 'who created you' in data1:
                speechtxt("i was created by zeeshan abubakar aiman and disha")

            elif 'where is J I T' in data1 or 'where is jit' in data1:
                speechtxt("neaar bada cross davangere")

            elif 'who is manjula ' in data1:
                speechtxt("she is our python teacher and because of her i came into existance because of her mini project")
        	
           
 
            elif "see you again"in data1:
                speechtxt("thank you,it was amazing to chit chat with you,have smile")
                break      
    else:
        print("thanks say my name properly ")
        speechtxt("Say my name properly...")
        
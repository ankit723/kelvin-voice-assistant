import speech_recognition as sr # recognise speech
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import os # to remove created audio files
import pyautogui #screenshot
import pyttsx3
import datetime
import wikipedia
from time import sleep

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name
        
def there_exists(terms):
    for term in terms:
        if term in (voice_data):
            return True

person_obj = person()
asis_obj = asis()
asis_obj_name = 'Kelvin: '
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Rate
engine.setProperty("rate", 200)
# volume
volume = engine.setProperty("volume", 1)

def engine_speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()
    

def kelvin_record_audio(ask=""):
    r = sr.Recognizer() # initialise a recogniser
    # listen for audio and convert it to text:
    with sr.Microphone() as source: # microphone as source
        if ask:
            print(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Kelvin is Recognising...")

        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print("I Didn't get that")
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print("You: ", voice_data.lower()) # print what user said
        return voice_data.lower()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("yes I am there! Good Morning!")
        #print(asis_obj_name+"yaa Iam there! Good Morning")

    elif hour>=12 and hour<17:
        speak("yes i am there! Good Afternoon!")   
        #print(asis_obj_name+"yaa Iam there! Good Afternoon")

    elif hour>=17 and hour<20:
        speak("yes i am there! Good evening!") 
        #print(asis_obj_name+"yaa Iam there! Good Evening!") 

    else:
        speak("yes i am  there! Good night!")
        #print(asis_obj_name+"yaa Iam there! Good night!")

    speak_to_acknoledge = ["what are the things you can do for me?","what can you do for me?","do some thing for me?","help me?","what are the things you can do?","what can you do?"]
    acknoledgement = speak_to_acknoledge[random.randint(0,len(speak_to_acknoledge)-1)]
    speak("you can try asking" + acknoledgement)
    
def google_new_tab():
    pyautogui.hotkey('ctrl', 't')
    
def google_close_tab():
    pyautogui.hotkey('ctrl', 'w')
    
def google_reload_tab():
    pyautogui.hotkey('ctrl', 'r')
    
def google_chrome_close():
    pyautogui.hotkey('alt', 'f4')
    
def google_switch_tab():
    pyautogui.hotkey('ctrl', 'tab')
    
def google_reopen_tab():
    pyautogui.hotkey('ctrl', 'shift', 't')
    
def windows_pause():
    pyautogui.hotkey('pause')
    
def windows_play():
    pyautogui.hotkey('play')
    
def windows_settings():
    pyautogui.hotkey('win', 'i')
    
def this_pc():
    pyautogui.hotkey('win', '3')
    
def clean_per_temp():
    os .startfile('C:\\Users\\studi\\AppData\\Local\\Temp')
    os .startfile('C:\\Windows\\Temp')
    pyautogui.hotkey('shift', 'delete')
    pyautogui.hotkey('ctrl', 'a')
    
def clean_temp():
    os .startfile('C:\\Windows\\Temp')
    pyautogui.hotkey('shift', 'delete')
    
def clean_manager():
    os.startfile('C:\\Users\\studi\\Desktop\\apps folder\\disk cleanup')
    sleep(10)
    pyautogui.hotkey('enter')
    sleep(15)
    pyautogui.hotkey('enter')
    
def windows_close():
    pyautogui.hotkey('alt', 'f4')
    sleep(2)
    pyautogui.hotkey('enter')
    
def run_uit():
    try:
        import speedtest
        speak('wait for a while i am checking it')
        speed = speedtest.Speedtest()
        upload = speed.upload()
        correctUp = int(int(upload)/80000)
        download = speed.download()
        correctDown = int(int(download)/80000)
        speak(f'downloading speed is {correctDown} mbps')
        speak(f'uploading speed is {correctUp} mbps')
        print(f'uploading speed is {correctUp} mbps')
    except speedtest.SpeedtestHTTPError:
        speak('sorry, but you are not connected with the internet ')
        
def respond(voice_data):
        if there_exists(["shutdown","shutdown computer"]):
            windows_close()

        if there_exists(["settings"]):
            windows_settings()    
            speak("opening settings")

        if there_exists(["play"]):
            windows_play()
        
        if there_exists(["pause"]):
            windows_pause()

        if there_exists(["clean temp files", "clean temporary files"]):
            clean_per_temp()
            clean_temp()
            speak("cleaned all temperory files")

        if there_exists(["clean disk manager"]):
            clean_manager()
            speak("cleaned disk manager")

        if there_exists(["new tab"]):
            google_new_tab()

        if there_exists(["close tab"]):
            google_close_tab()

        if there_exists(["reload", "reload tab"]):
            google_reload_tab

        if there_exists(["close chrome"]):
            google_chrome_close()

        if there_exists(["switch tab", "change tab"]):
            google_switch_tab()

        if there_exists(["reopen", "reopen closed tab"]):
            google_reopen_tab()

        # 1: greeting
        if there_exists(['hey','hi','hello','hai','whats up']):
            greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
            greet = greetings[random.randint(0,len(greetings)-1)]
            speak(greet)
        
        # 2: name
        if there_exists(["what is your name","what's your name","tell me your name"]):
            if person_obj.name:
                speak("whats with my name ")
            else:
                speak("i dont know my name . what's your name?")

        # 2: name
        if there_exists(["what are the things you can do for me","what can you do for me","do some thing for me","help me","what are the things you can do","what can you do"]):
      
            speak("I can play music for you!\nI can talk to you as a friend!\nYou can make me remember your name!\nYou can change my name according to your wish!\nI can tell you the exact time!\nI can open apps for you\nI can search the web for you!\nand many more?\n")
            

        if there_exists(["my name is"]):
            person_name = voice_data.split("is")[-1].strip()
            speak("okay, i will remember that " + person_name)
            person_obj.setName(person_name) # remember name in person object
        
        if there_exists(["your name should be", "your name is", 'you  are']):
            asis_name = voice_data.split("be")[-1].strip()
            speak("okay, i will remember that my name is " + asis_name)
            asis_obj.setName(asis_name) # remember name in asis object

        # 3: greeting
        if there_exists(["how are you","how are you doing"]):
            speak("I'm very well, thanks for asking " + person_obj.name)

        # says time

        if 'time' in voice_data:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # 6: search youtube
        if there_exists(["youtube"]):
            search_term = voice_data.split("for")[-1]
            url = "https://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            speak("Here is what I found for " + search_term + "on youtube")

        #7: get stock price
        if there_exists(["price of"]):
            search_term = voice_data.split("for")[-1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            speak("Here is what I found for " + search_term + " on google")
            
        
        # search for music
        if there_exists(["play"]):
            search_term= voice_data.split("for")[-1]
            url="https://open.spotify.com/search/"+search_term
            webbrowser.get().open(url)
            speak("You are listening to"+ search_term +"enjoy sir")

        #search for amazon.com
        if there_exists(["amazon.com"]):
            search_term = voice_data.split("for")[-1]
            url="https://www.amazon.in"+search_term
            webbrowser.get().open(url)
            speak("here is what i found for"+search_term + "on amazon.com")
            
            
        #make a note
        if there_exists(["make a note"]):
            search_term=voice_data.split("for")[-1]
            url="https://keep.google.com/#home"
            webbrowser.get().open(url)
            speak("Here you can make notes")
            
        #open instagram
        if there_exists(["open instagram","want to have some fun time","instagram"]):
            search_term=voice_data.split("for")[-1]
            url="https://www.instagram.com/"
            webbrowser.get().open(url)
            speak("opening instagram")

        #open facebook
        if there_exists(["facebook"]):
            search_term=voice_data.split("for")[-1]
            url="https://www.facebook.com/"
            webbrowser.get().open(url)
            speak("opening facebook")
            
        #open twitter
        if there_exists(["open twitter","twitter"]):
            search_term=voice_data.split("for")[-1]
            url="https://twitter.com/"
            webbrowser.get().open(url)
            speak("opening twitter")
            
        if there_exists(["open app", "open application"]):
            speak("which app should i open?")
            exe_app = kelvin_record_audio()
            speak("ok! opening"+ exe_app)
            try:
                os.startfile('C:\\Users\\studi\\Desktop\\apps folder\\'+exe_app)
            except Exception:
                speak("pleae say a valid name")
            
        #13 screenshot
        if there_exists(["capture","my screen","screenshot"]):
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save('C:\\Users\\studi\\Pictures\\Saved Pictures\\')
            speak("screenshot done") 

        #13 volume up
        if there_exists(["volume up", 'increase volume', 'increase the voulme']):
            pyautogui.press("volumeup")
            speak("increasing the volume")
            

        #13 volume up
        if there_exists(["volume down", 'decrease volune', 'decrease the volume']):
            pyautogui.press("volumedown")
            speak("decreasing the volume")    

        #13 volume up
        if there_exists(["volume mute","mute"]):
            pyautogui.press("volumemute")  
            speak("muting the volume")   
        
        
        #14 to search wikipedia for definition
        if there_exists(["definition of","define","wiki","wikipedia", "mean", "meaning"]):
            speak('Searching Wikipedia...')
            # query = query.replace("wikipedia", "")
            voice_data = voice_data.replace("wikipedia", "")
            # results = wikipedia.summary(query, sentences=2, )
            results = wikipedia.summary(voice_data, sentences=2, )
            speak("According to Wikipedia")
            speak(results)

        if there_exists(["check connection speed", "speed", "internet speed"]):
            run_uit()

        if there_exists(["exit", "quit", "goodbye", "bye"]):
            speak("we could continue more, but....,,,,,..,,,,, byee")
            exit()
        
if __name__ == "__main__":
    wishMe()
 
while True:
    voice_data = kelvin_record_audio("Listening") 
    respond(voice_data)

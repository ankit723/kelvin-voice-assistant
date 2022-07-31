import playsound # to play an audio files
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
import pyautogui #screenshot
import pyttsx3
import wikipedia
import random
from playsound import playsound
import datetime
import os
import ascii_magic
import cv2
import numpy as np

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
        if term in (r):
            return True

person_obj = person()
asis_obj = asis()
asis_obj_name = 'Kelvin: '
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Rate
engine.setProperty("rate", 200)
# volume
volume = engine.setProperty("volume", 1)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("yes i am there! Good Morning!")
        print(asis_obj_name+"yaa Iam there! Good Morning")

    elif hour>=12 and hour<17:
        speak("yes i am there! Good Afternoon!")   
        print(asis_obj_name+"yaa Iam there! Good Afternoon")

    elif hour>=17 and hour<20:
        speak("yes i am there! Good evening!") 
        print(asis_obj_name+"yaa Iam there! Good Evening!") 

    else:
        speak("yes i am there there! Good night!")
        print(asis_obj_name+"yaa Iam there! Good night!")

    speak_to_acknoledge = ["what are the things you can do for me?","what can you do for me?","do some thing for me?","help me?","what are the things you can do?","what can you do?"]
    acknoledgement = speak_to_acknoledge[random.randint(0,len(speak_to_acknoledge)-1)]
    speak("you can try asking" + acknoledgement)
    print(asis_obj_name+"If you want Chat with me as a friend, Type 'Sam'")
    speak("If you want Chat with me as a friend, Type 'Sam'")

def loadbwimage():
    IMAGE_PATH = input('path name')
    image = cv2.imread(IMAGE_PATH)
    image = cv2.resize(image,(100, 100), interpolation=cv2.INTER_AREA)

    brightness = np.empty((image.shape[0], image.shape[1]))
    ascii_image = [] 

    #Caclulate brightness values
    for x in range(len(image)):
        for y in range(len(image[x])):
            pixel = image[x][y]
            avg = (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) // 3
            brightness[x][y] = avg

    #Brightness to Ascii Values
    ascii_vals = [' ', '`','^','"',',',':',';','I','l','!','i','~','+','_','-','?',']',
            '[','}','{','1',')','(','|','/','t','f','j','r','x','n','u','v','c','z',
            'X','Y','U','J','C','L','Q','0','O','Z','m','w','q','p','d','b','k','h',
            'a','o','*','#','M','W','&','8','%','B','@','$']

    ascii_vals_brightness = {}
    val = 0
    increment = 1500 // len(ascii_vals)

    for x in ascii_vals:
        ascii_vals_brightness[(val, val + increment)] = x
        val += increment + 1

    # assigning values
    for x in range(len(brightness)):
        temp = []
        for y in range(len(brightness[x])):
            val = brightness[x][y]
            for low, high in ascii_vals_brightness.keys():
                if val >= low and val <= high:
                    temp.append(ascii_vals_brightness[(low, high)])
                    break
        ascii_image.append(temp)

    #Printing it out!
    for row in ascii_image:
        line = [x+x for x in row]
        print("".join(line))
    exit_code = input("type quit to exit: ")
    if "quit" in exit_code:
        respond()

def loadcolorimage():
    output = ascii_magic.from_image_file(input('path name: '),columns = 100, char = '#')
    ascii_magic.to_terminal(output)
    exit_code = input("type quit to exit: ")
    if quit in exit_code:
        respond()

def respond(r):

    if there_exists(["convert image"]):
        a = input("which type of image do you want black and white or coloured image")
        if "black and white" in a or "black" in a:
            loadbwimage()
        if "colour" in a or "color" in a :
            loadcolorimage()


    # 1: greeting
    if there_exists(['hey','hi','hello','hai','whats up']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)
        print(asis_obj_name+greet)
    
    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("whats with my name ")
            print(asis_obj_name+"whats with my name ")
        else:
            speak("i dont know my name . what's your name?")
            print(asis_obj_name+"i dont know my name . what's your name?")

    # 2: name
    if there_exists(["what are the things you can do for me","what can you do for me","do some thing for me","help me","what are the things you can do","what can you do"]):
        print(asis_obj_name+"I can play music for you\nI can talk to you as a friend\nYou can make me remember your name\nYou can change my name according to your wish\nI can tell you the exact time\nI can open apps for you\nI can search the web for you\nand many more?\n")
        speak("I can play music for you!\nI can talk to you as a friend!\nYou can make me remember your name!\nYou can change my name according to your wish!\nI can tell you the exact time!\nI can open apps for you\nI can search the web for you!\nand many more?\n")
           

    if there_exists(["my name is"]):
        person_name = r.split("is")[-1].strip()
        speak("okay, i will remember that " + person_name)
        print(asis_obj_name+"okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    
    if there_exists(["your name should be"]):
        asis_name = r.split("be")[-1].strip()
        speak("okay, i will remember that my name is " + asis_name)
        print(asis_obj_name+"okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) # remember name in asis object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        speak("I'm very well, thanks for asking " + person_obj.name)
        print(asis_obj_name+"I'm very well, thanks for asking " + person_obj.name)

    # says time

    if 'time' in r:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")
        print(f"Sir, the time is {strTime}")

    # opens vs code

    if 'open code' in r:
        codePath = "C:\\Users\\studi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        speak("opening visual studio code")
        print("opening visual studio code")
            
    # opens google

    if 'open google' in r:
        codePath = "D:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(codePath)   
        speak("opening google chrome") 
        print(asis_obj_name+"opening google chrome")

    # opens blender

    if 'open blender' in r:
        codePath = "C:\\Program Files\\Blender Foundation\\Blender 2.92\\blender.exe"
        os.startfile(codePath)    
        speak("opening blender")
        print(asis_obj_name+"opening blender")    

    # opens unity

    if 'open unity' in r:
        os.startfile(codePath)    
        codePath = "C:\\Program Files\\Unity Hub\\Unity Hub.exe"
        speak("opening unity hub")  
        print(asis_obj_name+"opening unity hub")           

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it, time"]):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")
        print(f"Sir, the time is {strTime}")

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in r:
        search_term = r.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        speak("Here is what I found for" + search_term + "on google")
        print(asis_obj_name+"Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = r.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        speak("Here is what I found for " + search_term + "on youtube")
        print(asis_obj_name+"Here is what I found for " + search_term + "on youtube")

    #7: get stock price
    if there_exists(["price of"]):
        search_term = r.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        speak("Here is what I found for " + search_term + " on google")
        print(asis_obj_name+"Here is what I found for " + search_term + " on google")
    
    # search for music
    if there_exists(["play"]):
        search_term= r.split("for")[-1]
        url="https://open.spotify.com/search/"+search_term
        webbrowser.get().open(url)
        speak("You are listening to"+ search_term +"enjoy sir")
        print(asis_obj_name+"You are listening to"+ search_term +"enjoy sir")

    #search for amazon.com
    if there_exists(["amazon.com"]):
        search_term = r.split("for")[-1]
        url="https://www.amazon.in"+search_term
        webbrowser.get().open(url)
        speak("here is what i found for"+search_term + "on amazon.com")
        print(asis_obj_name+"here is what i found for"+search_term + "on amazon.com")
         
    #make a note
    if there_exists(["make a note"]):
        search_term=r.split("for")[-1]
        url="https://keep.google.com/#home"
        webbrowser.get().open(url)
        speak("Here you can make notes")
        print(asis_obj_name+"Here you can make notes")
        
    #open instagram
    if there_exists(["open instagram","want to have some fun time","instagram"]):
        search_term=r.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        speak("opening instagram")
        print(asis_obj_name+"opening instagram")

    #open facebook
    if there_exists(["facebook"]):
        search_term=r.split("for")[-1]
        url="https://www.facebook.com/"
        webbrowser.get().open(url)
        speak("opening facebook")
        print(asis_obj_name+"opening facebook")
        
    #open twitter
    if there_exists(["open twitter","twitter"]):
        search_term=r.split("for")[-1]
        url="https://twitter.com/"
        webbrowser.get().open(url)
        speak("opening twitter")
        print(asis_obj_name+"opening twitter")

    if there_exists(["open app", "open application"]):
        speak("which app should i open?")
        exe_app = input(asis_obj_name+"which app shoulod I open?")
        speak("ok! opening"+ exe_app)
        print(asis_obj_name+"ok! opening"+ exe_app)
        try:
            os.startfile('C:\\Users\\studi\\Desktop\\apps folder\\'+exe_app)
        except Exception:
            print(asis_obj_name+"pleae say a valid name")
            speak("pleae say a valid name")
        
    #9 weather
    if there_exists(["weather","tell me the weather report","whats the condition outside"]):
        search_term = r.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        speak("Here is what I found for on google")
        print(asis_obj_name+"Here is what I found for on google")
    
        
    #13 screenshot
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:\\Users\\studi\\Pictures\\Saved Pictures\\')
        speak("screenshot done") 
        print(asis_obj_name+"screenshot done") 

    #13 volume up
    if there_exists(["volume up", 'increase volume', 'increase the voulme']):
        pyautogui.press("volumeup")
        speak("increasing the volume")
        print(asis_obj_name+"increasing the volume")

    #13 volume up
    if there_exists(["volume down", 'decrease volune', 'decrease the3 volume']):
        pyautogui.press("volumedown")
        speak("decreasing the volume")    
        print(asis_obj_name+"decreasing the volume")

    #13 volume up
    if there_exists(["volume mute","mute"]):
        pyautogui.press("volumemute")  
        speak("muting the volume")   
        print(asis_obj_name+"muting the volume")
    
    
    #14 to search wikipedia for definition
    if there_exists(["definition of","define","wiki","wikipedia", "mean", "meaning"]):
        speak('Searching Wikipedia...')
        # query = query.replace("wikipedia", "")
        r = r.replace("wikipedia", "")
        # results = wikipedia.summary(query, sentences=2, )
        results = wikipedia.summary(r, sentences=2, )
        speak("According to Wikipedia")
        print(asis_obj_name+results)
        speak(results)

    if there_exists(["exit", "quit", "goodbye", "bye"]):
        speak("we could continue more, but....,,,,,..,,,,, byee")
        print(asis_obj_name+"we could continue more, but. bye")
        exit()

if __name__ == "__main__":
    wishMe()
    # get_response()
    
while(1):
    r = input("Ask: ") # get the voice input
    respond(r) # respond
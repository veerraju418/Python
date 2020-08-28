#Text to Speech
#pip install pyttsx3
import pyttsx3 as p
engine=p.init()
inp=input('Name-->')
engine.say('Welcome'+inp)
engine.runAndWait()

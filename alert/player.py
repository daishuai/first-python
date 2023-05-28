import pyttsx3
from playsound import playsound

pt = pyttsx3.init()
pt.say('苏州市相城区元和街道发生五级警情')
pt.runAndWait()

playsound('Monsters.mp3')

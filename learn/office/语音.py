import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.say('宝宝 宝宝 该起床了')
engine.runAndWait()
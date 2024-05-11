import pyttsx3

enigine = pyttsx3.init()

def Say(text):
    enigine.say(text)
    enigine.runAndWait()


Say("Hi This is Python")


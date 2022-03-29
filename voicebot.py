import speech_recognition as sr
import pyttsx3
import os


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
             #if 'alexa' in command:
             #command = command.replace('alexa','')
            print (command)

    except:
         pass            
    return command   
          
def run():
    command = take_command()
    if 'present' in command:
        talk('presenting the presentation')
        os.system(' start presentation.pptx')

run()         

import speech_recognition as gg
import pyttsx3
import pywhatkit

listener = gg.Recognizer()
engine = pyttsx3.init()
engine.say('fff')
engine.say('goof')
engine.runAndWait()

def take_command():
     try:
         with gg.Microphone() as source:
             print('listening.....')
             voice = listener.listen(source)
             command = listener.recognize_google(voice)
             command = command.lower()
             if 'imobot' in command:
                 command = command.replace('imobot','')
                 print(command)
     except:
        pass
     return command

def run_imobot():

    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        print('ok sir let me play'+song)
        pywhatkit.playonyt('play')


run_imobot()
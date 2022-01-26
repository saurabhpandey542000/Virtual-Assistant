# firstly to make an virtual assistent ,then first step is , to talk to Alexa --->  so we import speech recognizition package
import speech_recognition as sr
import pyttsx3

# Now , here in our Alexa Someone here to listen our Voice (Recognized our voice )
listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

engine.say('hey, Mr Saurabh')
engine.say('What Can I do For you')
engine.runAndWait()
# Here we use try block bcz suposed sometime Microphone might not be work Or give me Some other trouble -->

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening......')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:

                print(command)

        # if you don't need to try anything  then it "exept" it and "pass" it -->
    except:
        pass
    return command



import pyttsx3
import webbrowser
import datetime
import pyjokes
import speech_recognition as sr



def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print('plese speak now listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
              print("not understand")




# text to speech
def speechtx(y):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(y)
    engine.runAndWait()



if __name__ == '__main__':

    if sptext().lower() == 'hello nobita':
        b='ha bolo kiya hua'
        speechtx(b)
        data1=sptext().lower()
        if 'your name' in data1:
            speechtx('my name is nobita doraemon is my best friend')
        elif 'best friend' in data1:
            speechtx('doraemon is my best friend')
        elif 'enemy' in data1:
            speechtx('eeeee sooniyo and ziyan is my enemy')
        elif 'time' in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif 'youtube' in data1:
            webbrowser.open('https://www.youtube.com')
        elif 'google' in data1:
            webbrowser.open('https://www.google.com')
        elif 'instagram' in data1:
            webbrowser.open('https://www.instagram.com')
        elif 'facebook' in data1:
            webbrowser.open('https://www.facebook.com')
        elif 'twitter' in data1:
            webbrowser.open('https://www.twitter.com')
    else:
        print('not okk')
    
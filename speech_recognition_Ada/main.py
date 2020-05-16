import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()


def get_audio(ask=False):                    # if a text is passed to this function ask becomes true and audio is played
    with sr.Microphone() as source:
        if ask:
            professor_speak(ask)
        audio = r.listen(source, phrase_time_limit=4)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            professor_speak('Sorry , I did not get that')
        except sr.RequestError:
            professor_speak('Sorry, my speech service is down')
    return voice_data


def professor_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'  # give a random name to audio file
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def response(voice_data):
    if 'what is the time' in voice_data:
        professor_speak(ctime())

    if ' play music' in voice_data:
        music = get_audio('what do you want to listen to ?')
        url = 'https://youtube.com/results?search_query=' + music
        webbrowser.get().open(url)
        professor_speak(' Here is what I found for' + music)

    if 'find' in voice_data:
        index = voice_data.index('find')
        text = voice_data.split()[index + 1:]
        url = 'https://google.com/search?q=' + '+'.join(text)
        webbrowser.get().open(url)
        professor_speak('Here is what I found for' + ' '.join(text))

    if 'open' in voice_data:
        if 'chrome' in voice_data:
            professor_speak('Opening Google Chrome')
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')


    if 'find location' in voice_data:
        location = get_audio('what is the location?')
        url = 'https://google.nl/map/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        professor_speak('Here is the location of ' + location)

    if 'exit' in voice_data:
        professor_speak(" Adios " + name)
        exit()


if __name__ == "__main__":
    professor_speak("Hello , I am Max. what is your name?")
    name = get_audio()
    professor_speak("Hi, " + name + " how can I help you?")
    while 1:
        voice_data = get_audio()
        response(voice_data)

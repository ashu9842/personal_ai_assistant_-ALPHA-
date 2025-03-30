
import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi="<Your Key Here>"



def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    
    pygame.mixer.init()  # Initialize Pygame mixer

  
    pygame.mixer.music.load('temp.mp3') # Load the MP3 file

    
    pygame.mixer.music.play()  # Play the MP3 file

    
    while pygame.mixer.music.get_busy(): # Keep the program running until the music stops playing
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    

def ai(command):
    client = OpenAI(
    api_key="<Your API key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "system", "content": "This is a virtual assistant Alpha gives short responses"},
        {"role": "user", "content": command}
    ]
    )

    return (completion.choices[0].message.content)




def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    elif c.lower().startswith("guess"):
        song = c.lower().split(" ")[1]
        link = music.music[song]
        webbrowser.open(link)

    elif "news" in  c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code==200:
            #Parse the JSON response
            data=r.json()

            #Extract the articles
            articles = data.get('articles',[])

            #speak the headlines

            for article in articles:
                speak(article['title'])

    else:
          # Let OpenAI handle the request
          output = ai(c)
          speak(output)







    




if __name__ == "__main__":
    speak("Initializing Alpha....")
    while True:
        # Listen for the wake word "Alpha"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "alpha"):
                speak("Yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("Alpha Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error {0}".format(e))

    

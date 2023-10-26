import pandas as pd
import pyttsx3
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if 'es' in voice.languages:
        engine.setProperty('voice', voice.id)
        break

df = pd.read_excel('item/es3.xlsx')
words = df['Spanish'].tolist()

while True:
    word = random.choice(words)
    engine.say(word)
    engine.runAndWait()
    spelling = input("Please enter your spelling: ")
    if spelling.lower() == word.lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct spelling is {word}")

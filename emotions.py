import speech_recognition as sr
import nltk
import pandas as pd
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import requests
from nltk.tokenize import word_tokenize
from LeXmo import LeXmo
from ML import *
from datetime import datetime
# import text2emotion as emotion

# # Read the audio file into an AudioFile object
def audio_emo(name):
    r = sr.Recognizer()
    with sr.AudioFile('D:\\Humane Diary\\'+name) as source:
         audio = r.record(source)
    
    # # Transcribe the audio file using the recognize_google method
    transcript = r.recognize_google(audio)
    emo=LeXmo.LeXmo(transcript)
    text=emo.pop('text')
    txt=text.split("\n")
    emotions=[]
    if len(txt)>1:
        for i in range(len(txt)):
            emotions.append(emotions_classifications(txt[i]))
        
        counts = [emotions.count('joy'),
                emotions.count('fear'),
                emotions.count('anger'),
                emotions.count('sadness'),
                emotions.count('disgust'),
                emotions.count('shame'),
                emotions.count('guilt')]

        return max(counts)

    else:
        return emotions_classifications(text)

def text_emo(text):
    txt=text.split("\n")
    emotions=[]
    current_dateTime = datetime.now()
    current_time = str(current_dateTime.year)+"_"+str(current_dateTime.month)+"_"+str(current_dateTime.day)+"_"+str(current_dateTime.hour)+"_"+str(current_dateTime.minute)
    if len(txt)>1:
        for i in range(len(txt)):
            emotions.append(emotions_classifications(txt[i]))
        
        counts = [emotions.count('joy'),
                emotions.count('fear'),
                emotions.count('anger'),
                emotions.count('sadness'),
                emotions.count('disgust'),
                emotions.count('shame'),
                emotions.count('guilt')]

        return max(counts), current_time

    else:
        return emotions_classifications(text), current_time
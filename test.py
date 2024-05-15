from pytube import YouTube
from openai import OpenAI
from os import environ
import streamlit as st
from pydub import AudioSegment
import pysrt

import google_translate
from google_translate import translate_english_to

OpenAI_API_KEY = st.secrets["OPENAI_API_KEY"]
maxDuration = st.secrets["LIMIT_DURATION"]
client = OpenAI(api_key=OpenAI_API_KEY)


#1 Extract Audio from Youtube Video
# url = 'https://www.youtube.com/watch?v=BZP1rYjoBgI'
# video = YouTube(url)
# audio_path = 'audio_extract.mp3'

# try:
#     stream = video.streams.filter(only_audio=True).first()
#     stream.download(filename=f'./temp/' + audio_path)
#     print("The video is downloaded in MP3")
# except KeyError:
#     print(
#         "Unable to fetch video information. Please check the video URL or your network connection."
#     )

# audio_file = open(audio_path, "rb")


#2 Get SRT
# def CreateSRT(file_path):
#     with open(file_path, "rb") as audio_file:
#         transcription = client.audio.transcriptions.create(
#             model="whisper-1", 
#             file=audio_file, 
#             response_format="srt"
#         )
#     with open("temp/transcript.srt", "w") as transcript_file:
#         transcript_file.write(transcription)
        

# audio_file_path = "./temp/audio_extract.mp3"
# CreateSRT(audio_file_path)

#3 Translate SRT
input_srt = 'temp/transcript.srt'
subs = pysrt.open(input_srt, encoding='utf-8')

for sub in subs:
    translatedSub = translate_english_to(sub.text, 'yo')
    sub.text = translatedSub

subs.save('temp/translated.srt', encoding='utf-8')
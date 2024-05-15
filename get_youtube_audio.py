from pytube import YouTube
from openai import OpenAI
from os import environ
import vectara
import google_translate
import streamlit as st

OpenAI_API_KEY = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=OpenAI_API_KEY)


def prepForVectara():
    vectara.ResetCorpus()
    vectara.AddVideoTranscription()

def get_english_transcription_from_english_youtube(url):
    video = YouTube(url)
    try:
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=f"input_video.mp3")
        print("The video is downloaded in MP3")
    except KeyError:
        print(
            "Unable to fetch video information. Please check the video URL or your network connection."
        )

    audio_file = open("input_video.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", file=audio_file
    )

    english_transcription = transcription.text
    yoruba_transcription = google_translate.translate_english_to_yoruba(english_transcription)

    # Write transcription to file
    with open("video_transcription.txt", "w", encoding="utf-8") as file:
        file.write(yoruba_transcription)
    
    print("Text has been written to video_transcription.txt")

    prepForVectara()
    

    return yoruba_transcription


def askQuestionAboutVideo(prompt):
    english_answer =  vectara.askQuestion(prompt)
    yoruba_answer = google_translate.translate_english_to_yoruba(english_answer)
    return yoruba_answer






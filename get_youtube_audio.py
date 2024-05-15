from pytube import YouTube
from openai import OpenAI
from os import environ
import vectara
import google_translate
import streamlit as st
from pydub import AudioSegment

OpenAI_API_KEY = st.secrets["OPENAI_API_KEY"]
maxDuration = st.secrets["LIMIT_DURATION"]
client = OpenAI(api_key=OpenAI_API_KEY)

def get_duration_pydub(file_path):
   audio_file = AudioSegment.from_file(file_path)
   duration = audio_file.duration_seconds
   return duration

def prepForVectara():
    vectara.ResetCorpus()
    vectara.AddVideoTranscription()


def get_english_transcription_from_english_youtube(url, language):
    video = YouTube(url)
    try:
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=f"input_video.mp3")
        print("The video is downloaded in MP3")
    except KeyError:
        print(
            "Unable to fetch video information. Please check the video URL or your network connection."
        )

    audio_file_path = "input_video.mp3"
    audio_file = open(audio_file_path, "rb")
    duration = get_duration_pydub(audio_file_path)

    print("Duration: ", duration)
    if duration > maxDuration: 
        print("The video is too long. Please upload a video that is less than 5 minutes.")


    # transcription = client.audio.transcriptions.create(
    #     model="whisper-1", file=audio_file
    # )

    # english_transcription = transcription.text
    # yoruba_transcription = google_translate.translate_english_to_yoruba(
    #     english_transcription
    # )

    # # Write transcription to file
    # with open("video_transcription.txt", "w", encoding="utf-8") as file:
    #     file.write(yoruba_transcription)

    # print("Text has been written to video_transcription.txt")

    # prepForVectara()

    # if language == "English":
    #     return english_transcription

    # elif language == "Yoruba":
    #     return yoruba_transcription


def askQuestionAboutVideo(prompt, language):
    english_answer = vectara.askQuestion(prompt)
    yoruba_answer = google_translate.translate_english_to_yoruba(english_answer)

    print(language)
    if language == "English":
        return english_answer

    elif language == "Yoruba":
        return yoruba_answer

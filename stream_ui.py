import streamlit as st
from pytube import YouTube
from openai import OpenAI
from os import environ

OpenAI_API_KEY = environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OpenAI_API_KEY)

def get_english_transcription_from_youtube(url):
    try:
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename="input_video.mp3")
        audio_file = open("input_video.mp3", "rb")
        transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
        return transcription.text
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("YouTube Transcription")

    url = st.text_input("Enter the URL of the YouTube video")
    if st.button("Get Transcription"):
        if url:
            transcription = get_english_transcription_from_youtube(url)
            if transcription:
                st.write("Transcription:")
                st.write(transcription)
            else:
                st.write("Failed to fetch transcription.")
        else:
            st.write("Please enter a valid YouTube video URL.")

if __name__ == '__main__':
    main()

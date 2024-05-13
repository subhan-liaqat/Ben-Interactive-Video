from pytube import YouTube
from openai import OpenAI
from os import environ

OpenAI_API_KEY = environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OpenAI_API_KEY)


def get_english_transcription_from_english_youtube(video):
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

    return transcription.text


url = "https://www.youtube.com/watch?v=lXbEixkHcgc"
video = YouTube(url)
transcription = get_english_transcription_from_english_youtube(video)
print(transcription)

from pytube import YouTube
from openai import OpenAI
from os import environ
import vectara

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


url = "https://www.youtube.com/watch?v=JDSn2MuZUJI"
video = YouTube(url)
transcription = get_english_transcription_from_english_youtube(video)

print(transcription)

# Write transcription to file
with open("video_transcription.txt", "w") as file:
    file.write(transcription)

print("Text has been written to video_transcription.txt")


vectara.ResetCorpus()
vectara.AddVideoTranscription()

question = "What is her sidehustle?"
answer = vectara.askQuestion(question)

print(answer)

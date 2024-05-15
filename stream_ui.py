import streamlit as st
from pytube import YouTube
from openai import OpenAI
from os import environ
import get_youtube_audio
from streamlit_extras.stylable_container import stylable_container
import json
import random


OpenAI_API_KEY = environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OpenAI_API_KEY)

def main():
    
    st.title("Interactive Video")

    url = st.text_input("Enter the URL of the YouTube video")
    if st.button("Get Transcription"):
        if url:
            transcription = get_youtube_audio.get_english_transcription_from_english_youtube(url)
            if transcription:
                st.write("Transcription:")
                st.write(transcription)
            else:
                st.write("Failed to fetch transcription.")
        else:
            st.write("Please enter a valid YouTube video URL.")

    question_slot = st.empty()
    answer_slot = st.empty()


    with st.form('input_form'):
        # Place the text input and the button within the form
        col1, col2 = st.columns([5, 1])
        with col1:
            question = st.text_input("Ask a question:")
        with col2:
            st.write(" ")
            st.write(" ")
            submit_button = st.form_submit_button(label="Submit")

    # Check if the form has been submitted
    if submit_button:
        if question:
            print(get_youtube_audio.askQuestionAboutVideo(question))
           
        else:
            st.warning("Please enter a question.")



if __name__ == "__main__":
    main()
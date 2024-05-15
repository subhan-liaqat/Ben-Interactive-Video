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

    st.sidebar.title("Select Translation Language")
    language = st.sidebar.selectbox("Select Language", ["English", "Yoruba"])

    videoholder = st.empty()
    url = st.text_input("Enter the URL of the YouTube video")

    if 'video_url' not in st.session_state:
        st.session_state['video_url'] = None
    if 'transcription' not in st.session_state:
        st.session_state['transcription'] = None

    if st.button("Upload Video"):
        if url:
            transcription = get_youtube_audio.get_english_transcription_from_english_youtube(url, language)
            st.session_state['video_url'] = url
            st.session_state['transcription'] = transcription
        else:
            st.write("Please enter a valid YouTube video URL.")
    
    if st.session_state['video_url']:
        videoholder.video(st.session_state['video_url'])
        if st.session_state['transcription']:
            # st.write("Transcription:")
            with st.expander("Transcription:", expanded=False):
                st.write(st.session_state['transcription'])
            st.warning("Yoruba: Fidio rẹ ti jẹ ibaraenisepo, beere awọn ibeere nipa rẹ! \n English: Your video has been made interactive, ask questions about it!", icon="❔")
        else:
            st.write("Failed to fetch transcription.")
    
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
            answer = get_youtube_audio.askQuestionAboutVideo(question, language)
            st.write(answer)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()

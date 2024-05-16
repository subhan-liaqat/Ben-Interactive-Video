import streamlit as st

from streamlit_extras.stylable_container import stylable_container

st.title("Welcome To Ben Interactive Video 📺")

st.divider()

st.write("Introducing Ben Interactive Video: Video Interaction for Benin and Beyond We are proud to present Ben Interactive Video. Designed specifically for the Benin Multimodal AI Hackathon. Our innovative solution empowers users to interact with videos in their preferred language, saving time and breaking language barriers. also Creating new Media With Subtitles and Dubbing 🎥")

st.subheader("Features")

st.markdown(
    """
    📁 **Upload a video from YouTube:** Easily upload video from a Youtube URL\n
    💭 **Translate the video to Yoruba or French:** Create the full transcript translated into the selected language\n
    🎥 **Choose to have the video dubbed or subtitled or both:**  choose whether the video uploaded is subbed or dubbed into your selected langauge or both\n 
    📺 **Watch the translated video:** A New Video for the user to watch within the app\n
    """
)

st.subheader("How to Use")

st.markdown(
    """
    ✔ Select the tool you would like to use from the sidebar\n
    🌐 Enter the URL of the video you would like to interact with\n
    🌍 Select the language you would like to translate the video to\n
    🎥 Click the 'Upload Video' button\n
    🤖 Wait for the video to be processed\n
    📈 Profit
    """
)

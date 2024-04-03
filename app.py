import streamlit as st
import nltk
from gtts import gTTS
import os
import tempfile
from PIL import Image
import matplotlib.image as mpimg
import speech_recognition as sr
nltk.download('punkt')


def home():
  
    st.header("Home")
    st.title("Welcome to the Text and Speech Converter App!")
    st.write("This app allows you to convert text to speech and speech to text. Use the navigation bar on the left to access the different pages.")
    st.subheader(" Text to Speech : 🔊 🡢 📋")
    imageha = mpimg.imread('s_to_t3.webp') 
    st.image(imageha)
    st.write("Convert your text into speech. Simply type or paste your text into the input box and click 'Convert'. You can also choose the voice and adjust the speech rate.")
    st.subheader(" Speech to Text : 📋 🡢 🔊")
    imageha1 = mpimg.imread('t_to_s1.png') 
    st.image(imageha1) 
    st.write("Convert speech into text. Click the 'Start Recording' button to record your speech, and the app will transcribe it for you.")
    st.subheader("Start exploring the app and enjoy the convenience of converting text and speech!")
      
      
def text_to_speech(language='en'):
    st.title("Text to Speech Converter")
    imagehb = mpimg.imread('t_to_s-removebg.png')     
    st.image(imagehb)
    text = st.text_area("Enter text to convert to speech")
    sentences = nltk.sent_tokenize(text)


    if st.button("Convert to Speech"):
        if text:
            with tempfile.TemporaryDirectory() as tmpdir:
                audio_files = []

                for idx, sentence in enumerate(sentences):
                    tts = gTTS(text=sentence, lang=language, slow=False)
                    filename = f"output_{idx}.mp3"
                    filepath = os.path.join(tmpdir, filename)
                    tts.save(filepath)
                    audio_files.append(filepath)

                for file in audio_files:
                    st.audio(file, format='audio/mp3')

                for file in audio_files:
                    os.remove(file)
    else:
        st.warning("Please enter some text to convert.")

def speech_to_text():
    st.title("Speech to Text Converter")
    imagehb = mpimg.imread('s_to_t1.png')     
    st.image(imagehb)
    st.subheader("Click the button below and speak into your microphone to convert speech to text:")
    if st.button("Start Recording"):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
            st.write("Please speak now...")
            audio = recognizer.listen(source, timeout=5)  # Records audio from the microphone

        try:
            st.write("Recognizing...")
            text = recognizer.recognize_google(audio)  # Uses Google Speech Recognition
            st.write("You said:", text)
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            st.write("Sorry, an error occurred. Please check your internet connection.", e)

        
   

def main():
    st.set_page_config(layout="wide")
   
    tabs = ["Home", "Text To Speech","Speech To Text"]
    page = st.sidebar.selectbox("Select a page", tabs)
    if page == "Home":
        home()
    elif page == "Text To Speech":
        text_to_speech()
    elif page == "Speech To Text":
        speech_to_text()

if __name__ == "__main__":
    main()

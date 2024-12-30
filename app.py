import streamlit as st
import openai
import pyttsx3
import speech_recognition as sr
from PIL import Image

# Function to get AI responses using OpenAI GPT-3 or GPT-4
def get_ai_response(user_input):
    openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your OpenAI API key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Function for voice-to-text (Speech Recognition)
def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        return text

# Function for text-to-speech (pyttsx3)
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Streamlit app layout
st.title("Gen Z AI Chat App")
st.sidebar.header("Customizations")
theme_color = st.sidebar.color_picker("Pick a theme color", "#00FFFF")
font_style = st.sidebar.selectbox("Choose a font", ["Arial", "Verdana", "Comic Sans MS"])

# Avatar customization
uploaded_avatar = st.file_uploader("Upload Avatar Image", type=["png", "jpg", "jpeg"])
if uploaded_avatar:
    avatar_image = Image.open(uploaded_avatar)
    st.image(avatar_image, caption="Your Avatar", use_column_width=True)

# Profile customization
username = st.text_input("Enter your username", "GenZUser")
bio = st.text_area("Write your bio", "This is my Gen Z bio.")
if st.button("Save Profile"):
    st.write(f"Username: {username}")
    st.write(f"Bio: {bio}")

# Display the chat interface with customizable theme
st.markdown(f"""
    <style>
        .chatbox {{ font-family: '{font_style}', sans-serif; background-color: {theme_color}; }}
    </style>
    """, unsafe_allow_html=True)

# Input from user
user_input = st.text_input("Start chatting:", "")

if user_input:
    ai_response = get_ai_response(user_input)
    st.write(f"**You:** {user_input}")
    st.write(f"**AI:** {ai_response}")

# Option for multimedia (e.g., images)
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

# Button to reset chat
if st.button("Reset Chat"):
    st.experimental_rerun()

# Voice-to-Text and Text-to-Speech Integration
if st.button("Speak to Me"):
    text = voice_to_text()
    st.write(f"You said: {text}")
    response = get_ai_response(text)
    text_to_speech(response)
    st.write(f"AI says: {response}")

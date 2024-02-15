from openai import OpenAI
from config import openai_key
import json
import streamlit as st
from gtts import gTTS
import os

client = OpenAI(api_key=openai_key)

def ask_question(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a softBuilders assistant."},
            {"role": "user", "content": text}
        ]
    )
    content = response.choices[0].message.content
    return content

# Function to generate speech
def generate_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")


with open('data.json', 'r') as f:
    data = json.load(f)

st.title("SoftBuilders ChatBot")
user_question = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if user_question:
        found = False
        for item in data:
            if user_question.lower() in item["question"].lower():
                st.write(item["answer"])
                generate_speech(item["answer"])
                found = True
                break
        if not found:
            answer = ask_question(user_question)
            st.write(answer)
            generate_speech(answer)
    else:
        st.write("Please ask a question.")

# Play the generated speech
if os.path.exists("output.mp3"):
    st.audio("output.mp3", format="audio/mp3")
    os.remove("output.mp3")
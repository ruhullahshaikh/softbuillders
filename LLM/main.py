import streamlit as st
import json
from app import ask_question
with open('data.json', 'r') as f:
    data = json.load(f)

st.title("SoftBuilders ChatBot")
user_question = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if user_question:
        for item in data:
            if user_question.lower() == item["question"].lower():
                st.text(item["answer"])
                break
        else:
            # If not found in the JSON, ask ChatGPT
            st.text(ask_question(user_question))
    else:
        st.text("Please ask a question.")
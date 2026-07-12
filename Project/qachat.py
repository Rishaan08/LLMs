from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import requests

#Function to load suitable model and generate response
def get_model_response(question):
    api_key = os.getenv("OPENROUTER_API_KEY")

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json" 
    }

    #Add user message to history
    st.session_state["chat_history_api"].append({
        "role": "user",
        "content": question
    })

    payload = {
        "model": "nvidia/nemotron-3-super-120b-a12b:free",
        "messages": st.session_state["chat_history_api"]
    }

    reply = requests.post(
        url,
        headers=headers,
        json=payload
    )

    result = reply.json()
    response= result["choices"][0]["message"]["content"]

    #Store assistant response in history
    st.session_state["chat_history_api"].append({
        "role": "assistant",
        "content": response
    })
    return response

st.set_page_config(page_title="Q&A Conversational Chatbot")

st.header("Conversational Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Initialize API chat history
if "chat_history_api" not in st.session_state:
    st.session_state["chat_history_api"] = []

input = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

if submit and input:
    response = get_model_response(input)
    #Add user query and answer to session chat history
    st.session_state["chat_history"].append(("You", input))
    st.session_state["chat_history"].append(("Bot", response))
st.subheader("Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
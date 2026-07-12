#Q&A Chatbot
from langchain_community.llms import Ollama

from dotenv import load_dotenv
import os

load_dotenv()

import streamlit as st

#Function to load model and get response
def get_ollama_response(question):
    llm = Ollama(model='mistral', temperature=0.5)
    response = llm.invoke(question)
    return response

#Initialize streamlit app
st.set_page_config(page_title="Q&A Chatbot")
st.header("LangChain Application")

input = st.text_input("Input: ", key="input")
response = get_ollama_response(input)

submit = st.button("Ask")

#If Ask button is click
if submit:
    st.subheader("Response is")
    st.write(response)
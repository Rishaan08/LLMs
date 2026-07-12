from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#Langsmith Tracking
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

#Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful assistant. Provide concise and accurate answers.'),
        ('user','Question:{question}')
    ]
)

#Streamlit App
st.title('Chatbot with Ollama and Langchain')
input_text = st.text_input('Topic you want to learn about')

#Ollama LLM
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
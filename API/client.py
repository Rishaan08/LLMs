import requests
import streamlit as st

def get_llama3_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                            json={'input':{'topic':input_text}})
    data = response.json()
    return data['output']['content'] if isinstance(data['output'], dict) else data['output']

def get_mistral_response(input_text):
    response = requests.post("http://localhost:8000/explanation/invoke",
                             json={'input':{'topic':input_text}})
    
    return response.json()['output']

#Streamlit UI
st.title("Langchain Server with Ollama LLMs")
input_text = st.text_input("Write a poem on")
input_text1 = st.text_input("Provide explanation on")

if input_text:
    st.write(get_llama3_response(input_text))

if input_text1:
    st.write(get_mistral_response(input_text1))
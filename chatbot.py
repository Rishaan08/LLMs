from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
import streamlit as st 
import os
from dotenv import load_dotenv
load_dotenv()

# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Ollama"

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to user queries."),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, engine, temperature, max_tokens):
    llm = ChatOllama(model=engine, temperature=temperature, num_predict=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Select the Ollama Model
engine = st.sidebar.selectbox("Select Ollama Model", ["qwen2.5:7b", "llama3.1:8b", "llama3:8b ", "mistral:latest"])

# Adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Tokens", min_value=50, max_value=500, value=250)

# Main interface for user input
st.write("Ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, engine, temperature, max_tokens)
    st.write(response)
 
else:
    st.write("Please provide user input")
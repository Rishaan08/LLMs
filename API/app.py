from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title = "Langchain Server with Ollama",
    version = "1.0",
    description = "An API server using Langchain and Ollama LLM"
)

add_routes(
    app,
    Ollama(),
    path = "/ollama"
)

model1 = Ollama(model="llama3")

#Ollama Mistral LLM
llm = Ollama(model="mistral")

#Prompt Template
prompt1 = ChatPromptTemplate.from_template("Write a short poem about {topic}")
prompt2 = ChatPromptTemplate.from_template("Provide a detailed explanation about {topic}")

add_routes(
    app,
    prompt1 | model1,
    path = "/poem"
)

add_routes(
    app,
    prompt2 | llm,
    path = "/explanation"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
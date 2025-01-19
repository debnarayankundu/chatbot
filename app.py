from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st 
import os
from dotenv import load_dotenv
load_dotenv()

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","Your are a helpful assistant.Please provide response to user queries"),
        ("user","Ouestion:{question}")
    ]
)


st.title("Hii I'm Rishi.Ask your queries")
input_text=st.text_input("type your question")


llm=Ollama(model="llama3.2")
output_parser=StrOutputParser()

chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt


import os
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header("AI Research Tool")

# Get the absolute path to template.json
template_path = os.path.join(os.path.dirname(__file__), "template.json")
template = load_prompt(template_path)

user_input = st.text_input("Enter Your Prompt -> ")

if st.button("Send") and user_input:
    prompt = template.format(user_input=user_input)
    outputs = model.invoke(prompt)
    st.write(outputs.content)


# -*- coding: utf-8 -*-
"""chatbot app resume

"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install langchain-huggingface streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os
import streamlit as st

st.title("AI Chatbot")

hf_token = st.text_input("Enter HuggingFace API Token:", type="password")

if hf_token:
    os.environ['HUGGINGFACEHUB_API_TOKEN'] = hf_token

if "model" not in st.session_state:
        llm = HuggingFaceEndpoint(
            repo_id="meta-llama/Llama-3.2-3B-Instruct",
            task="text-generation",
            max_new_tokens=512,
            do_sample=False,
        )
        st.session_state.model = ChatHuggingFace(llm=llm)

if "messages" not in st.session_state:
        st.session_state.messages = []

for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:

        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        chat_history = [SystemMessage(content='You are a helpful AI assistant')]
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                chat_history.append(HumanMessage(content=msg["content"]))
            else:
                chat_history.append(AIMessage(content=msg["content"]))

        result = st.session_state.model.invoke(chat_history)

        with st.chat_message("assistant"):
            st.write(result.content)
        st.session_state.messages.append({"role": "assistant", "content": result.content})

else:
    st.warning("Please enter your HuggingFace API token to start chatting.")

!npm install -g localtunnel

import time
import subprocess

process = subprocess.Popen(
    ["streamlit", "run", "app.py", "--server.port=8501"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print("Starting Streamlit... Please wait 20 seconds")
time.sleep(20)
print("✅ Streamlit should be ready now!")

!npx localtunnel --port 8501


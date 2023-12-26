import streamlit as st
import time
#from ollama_handler import *
#from ollama_handler import generate_ollama_response
import ollama_handler

def clear_chat_history(messages):
    messages.clear()
    messages.append({"role": "assistant", "content": "What do you want to know about Sergio Hidalgo?"})

def handle_user_input(messages, prompt):
    if prompt:
        messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

def generate_response_if_needed(ollama, messages, prompt):
    if messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            response = ollama_handler.generate_ollama_response(ollama, messages, prompt)
            placeholder = st.empty()
            full_response = ''
            for char in response:  # Assume response is a string
                full_response += char
                placeholder.markdown(full_response)
                time.sleep(0.005)  # Adjust the delay as needed
        message = {"role": "assistant", "content": full_response}
        messages.append(message)


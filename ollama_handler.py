from langchain.llms import Ollama
import requests

def initialize_ollama():
    url = "http://192.168.1.241:11434"
    try:
        response = requests.get(url)
    except:
        url = "http://127.0.0.1:11434"
    return Ollama(base_url=url,model="mistral-resume")

def generate_ollama_response(ollama, messages, prompt_input):
    string_dialogue = "You are not Sergio Hidalgo but their assistant. Whenever anyone asks about Sergio refer to him as he or him. Try to be polite and precise with the information you give so he can get the job he is being interviewed for"
    for dict_message in messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    response = ollama.__call__(prompt=f"{string_dialogue} {prompt_input} Assistant: ")
    return response


from langchain.llms import Ollama

def initialize_ollama():
    return Ollama(base_url="http://192.168.1.26:11434",model="orca-resume")

def generate_ollama_response(ollama, messages, prompt_input):
    string_dialogue = "You are not Sergio Hidalgo but their assistant. Whenever anyone asks about Sergio refer to him as he or him"
    for dict_message in messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    response = ollama.__call__(prompt=f"{string_dialogue} {prompt_input} Assistant: ")
    return response


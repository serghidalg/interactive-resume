from langchain.llms import Ollama
import requests
import variables

def initialize_ollama():
    url = variables.url
    try:
        response = requests.get(url)
    except:
        url = variables.url2
    return Ollama(base_url=url,model=variables.model_name)

def generate_ollama_response(ollama, messages, prompt_input):
    string_dialogue = variables.instructions
    for dict_message in messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    response = ollama.__call__(prompt=f"{string_dialogue} {prompt_input} Assistant: ")
    # Should make interactive-resume not show the thinking steps
    response = re.sub(r"<think>.*?</think>\n?", "", response, flags=re.DOTALL).strip()
    return response


import streamlit as st
import ollama_handler
import session_logic
import ui

# App title
st.set_page_config(page_title="Sergio's CV")
with st.sidebar:
    ui.setup_sidebar()

ollama = ollama_handler.initialize_ollama()

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "What do you want to know about Sergio Hidalgo?"}]

if st.sidebar.button('Clear Chat History', on_click=lambda: session_logic.clear_chat_history(st.session_state.messages)):
    pass

prompt = st.chat_input()

session_logic.handle_user_input(st.session_state.messages, prompt)

ui.display_messages(st.session_state.messages)

session_logic.generate_response_if_needed(ollama, st.session_state.messages, prompt)

#ui.display_messages(st.session_state.messages)


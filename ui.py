import streamlit as st

def setup_sidebar():
    st.title("Sergio Hidalgo")
    st.subheader("Curriculum Vitae")
    st.markdown("Relevant links:")
    st.markdown("- [LinkedIn](https://www.linkedin.com/in/serghidalg/)")
    st.markdown("- [Github](https://www.github.com/serghidalg)")

def display_messages(messages):
    for message in messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


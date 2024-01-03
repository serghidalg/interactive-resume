import streamlit as st
import variables

def setup_sidebar():
    st.image(variables.picture)
    st.title(variables.name)
    st.subheader("Curriculum Vitae")
    st.markdown("Relevant links:")
    st.markdown(f"- [LinkedIn]({variables.url_linkedin})")
    st.markdown(f"- [Github]({variables.url_github})")
    st.markdown(f"- [CV]({variables.url_cv})")

def display_messages(messages):
    for message in messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


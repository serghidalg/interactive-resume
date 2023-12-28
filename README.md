# Interactive Resume with Streamlit and Ollama

## Overview

This project aims to create an interactive resume using Streamlit, a Python library for building web applications, and Ollama, a language model for conversational AI. The interactive resume allows users to engage in a conversation with an AI assistant to learn more about a person's qualifications, experience, and other relevant information typically found in a resume.

## Features

- **Streamlit Interface:** Utilizes Streamlit to create a user-friendly interface for interaction.
- **Ollama Integration:** Incorporates Ollama, a language model, to generate conversational responses.
- **Chat-Based Interaction:** Enables users to ask questions and receive responses in a conversational format.
- **Clear and Informative:** Provides relevant links and information about the person whose resume is being presented.

## How to Run

To run the project locally, follow these steps:

1. **Clone the Repository:** 
   ```bash
   git clone https://github.com/yourusername/interactive-resume.git
   ```
2. **Install Dependencies:**
   ```bash
   cd interactive-resume
   pip install -r requirements.txt
   ```
3. **Run the Application:**
   ```bash
   streamlit run main.py
   ```

*Note:* There is a streamlit_cv.service file which can be useful to some people in the files folder.

## Usage

- Upon launching the application, you'll see a sidebar with relevant links and the conversation area.
- Users can input questions or prompts in the chat input area.
- The AI assistant (powered by Ollama) will respond to user queries, creating an interactive conversation.



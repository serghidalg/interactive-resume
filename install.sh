#!/bin/bash

# Is python3 installed?
if command -v python3 &>/dev/null; then
    python_executable="python3"
elif command -v python &>/dev/null; then
    python_executable="python"
else
    echo "Python 3 is not installed. Exiting."
    exit 1
fi

# Creating virtual environment
$python_executable -m venv venv

# Entering virtual environment
source venv/bin/activate

# Installing pip packages
pip install -r requirements.txt

# Running the setup of variables
$python_executable setup_variables.py

# Performing a test run :D
streamlit run main.py

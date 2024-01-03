#!/bin/sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python setup_variables.py

FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY *py ./
RUN mkdir files
COPY files/* files/

EXPOSE 8501
CMD ["streamlit","run","main.py"]


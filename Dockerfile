FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y

RUN pip install -r requirements.txt

EXPOSE 8501
ENTRYPOINT [ "streamlit", "run" ]
CMD [ "app.py" ]
FROM python:3.10.0rc1-buster

WORKDIR     /flask-app

COPY        requirements.txt .

RUN         pip install -r requirements.txt

COPY        . .

ENTRYPOINT [ "python", "app.py" ]
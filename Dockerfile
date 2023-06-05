FROM python:3.7.8-slim

COPY requirements.txt requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

COPY ./backend /app/backend
COPY ./bin /app/bin
COPY wsgi.py /app/wsgi.py
WORKDIR /app

RUN useradd flaskUser
USER flaskUser

EXPOSE 8080

ENTRYPOINT ["bash", "/app/bin/start.sh"]
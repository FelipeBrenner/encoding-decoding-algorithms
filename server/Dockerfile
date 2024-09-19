FROM python:3.9-alpine

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /app
ADD src/*.py /app/
WORKDIR /app
ENV FLASK_APP=app.py FLASK_DEBUG=1 PYTHONUNBUFFERED=1

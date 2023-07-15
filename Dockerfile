FROM python:3.10-slim

WORKDIR /app
RUN apt-get update

COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
ENTRYPOINT ./start.sh

# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP="main.py"
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
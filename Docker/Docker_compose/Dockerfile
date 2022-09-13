FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install flask
WORKDIR ./
COPY ./app.py /app.py
CMD python3 app.py
FROM ubuntu:latest
RUN apt-get update && \ 
apt-get install -y \
python3 \
python3-pip && \
pip install flask
WORKDIR ./
COPY ./app.py /app.py
CMD python3 app.py
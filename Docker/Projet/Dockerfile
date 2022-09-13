FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install flask
RUN pip install pandas
WORKDIR ./
COPY ./app.py /app.py
COPY ./myfile.csv /myfile.csv
CMD python3 app.py
#RUN echo “I am run during image building”
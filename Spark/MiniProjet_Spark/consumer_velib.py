from email import header
from kafka import KafkaConsumer
import json
import csv
from csv import writer
from datetime import datetime
import pandas as pd


topic_name = 'vlib_status_ville'

consumer = KafkaConsumer(
     topic_name,
     bootstrap_servers=['51.38.185.58:9092'],
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

current_date_time = datetime.now()


data = []
for message in consumer:
    data.append(message.value['fields'])
    if len(data) >= 10:
        res = pd.DataFrame(data)
        res.to_csv('data_velib.csv', mode ='a', index = False, header = False)

        data = []
    print(message)
import requests

import time
from time import strftime, localtime
#src: https://datacorner.fr/velib/

base_url = "https://opendata.paris.fr/api/records/1.0/search/"
dataset  = "velib-disponibilite-en-temps-reel"
facet    = "&facet=overflowactivation&facet=creditcard&facet=kioskstate&facet=station_state"
def get_data(nbrows):

    url = base_url + "?dataset=" + dataset + "%40parisdata&rows=" + str(nbrows) + facet
    mytime = strftime("%Y-%m-%d %H:%M:%S", localtime())
 
    resp = requests.get(url)

    data = resp.json()
    data['timestamp'] = mytime

    return data

def get_producer(ip, port=9092):
    
    from kafka import KafkaProducer
    import json

    broker = "{ip}:{port}".format(ip=ip, port=port)
    print("connecting to ", broker)
    producer = KafkaProducer(
                    bootstrap_servers=[broker], 
                    value_serializer= lambda x:json.dumps(x).encode('utf-8')
                )
    return producer

def send_records_to_kafka(producer, topic, records):
    
    for record in records:
        print('sending record')
        producer.send(topic, record)

ip="51.38.185.58"
producer = get_producer(ip)
topic = "vlib_status_ville"

while True:
    example = get_data(nbrows=20)
    send_records_to_kafka(producer, topic, example['records'])
    print("waiting 60 seconds for next records")
    time.sleep(60)
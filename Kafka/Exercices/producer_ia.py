from email import message
from kafka import KafkaProducer
import json 

#producer = KafkaProducer()

producer = KafkaProducer(bootstrap_servers=['51.38.185.58:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

topic = "prediction_caillau"

item = [[100,2]]

#producer.send(topic, item)

#Utilisation des partitions (0 ou 1)
producer.send(topic, partition=0,value=item)

#Permet d'envoyer le message sans attendre que le buffer soit rempli
producer.flush()
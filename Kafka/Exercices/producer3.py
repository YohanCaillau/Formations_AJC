from kafka import KafkaProducer
import random

topic="caillau"

producer= KafkaProducer(bootstrap_servers=['51.38.185.58:9092'])

def programme():
    n = random.randint(0,1)
    return n

message="salut, c'est yohan".encode("utf-8")

producer.send(topic, partition=programme(),value=message)

#Permet d'envoyer le message sans attendre que le buffer soit rempli
producer.flush()




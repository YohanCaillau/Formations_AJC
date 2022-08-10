from kafka import KafkaProducer
import json
import time
from get_temperature import get_temperature_data


topic = "caillau_exo10" 

producer = KafkaProducer(    
        bootstrap_servers=['127.0.0.1:9092'],
        value_serializer=lambda value: json.dumps(value).encode('utf-8')
        )

while True:
        data = {
    'temperatures': [
            get_temperature_data()
           ] 
        }
        var=data.get('temperatures')
        producer.send(topic, var)
        producer.flush()
        time.sleep(0.5)

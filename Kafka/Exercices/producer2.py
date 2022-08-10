from kafka import KafkaProducer
import json


producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

topic="caillau"

message={"data":[[1, 2,], [3, 4]]}

producer.send(topic, message 
             )
producer.flush()


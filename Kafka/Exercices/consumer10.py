import json 
import numpy as np
from kafka import KafkaConsumer

topic_name = "caillau_exo10" 
 
consumer = KafkaConsumer(
    topic_name, 
    bootstrap_servers=["127.0.0.1:9092"],
    value_deserializer= lambda byte_data: json.loads(byte_data.decode('utf-8')) 
)

temperatures = []

for message in consumer:
    temperature = message.value
    temperatures.append(temperature)
    print(temperatures)

    if len(temperatures) >=10:
        array_temp = np.array(temperatures)
        moyenne = array_temp.mean()
        écart = np.std(array_temp)
        print(f"La moyenne est de : {moyenne} et l'écart_type est de : {écart}")

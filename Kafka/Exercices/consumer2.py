from kafka import KafkaConsumer
import json  
import numpy as np

topic='caillau'

consumer = KafkaConsumer(topic, bootstrap_servers=['127.0.0.1:9092'], value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    message=message.value
    print(message)
    print(type(message))
    # to return a group of the key-value
    # pairs in the dictionary
    result = message.items()
    # Convert object to a list
    data = list(result)
    # Convert list to an array
    numpyArray = np.array(data, dtype=object)
    # print the numpy array
    #print(numpyArray)
    #print(type(numpyArray))
    #s = np.sum(numpyArray, axis=0)
    #print(s)

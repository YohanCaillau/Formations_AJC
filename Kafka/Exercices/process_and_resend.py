import json
import numpy as np
from kafka import KafkaProducer
from kafka import KafkaConsumer

def test(numpyarray):
    somme = np.sum(numpyarray, axis=0)
    return somme

json_file =  {"pi":3.14, 
              "g":9.81, 
              "v_son":340
             }

# to return a group of the key-value
# pairs in the dictionary
result = json_file.items()
# Convert object to a list
data = list(result)
# Convert list to an array
numpyArray = np.array(data, dtype=object)
# print the numpy array
#print(numpyArray)

#print(test(numpyArray))

message = str((test(numpyArray)))
message = message.encode("utf-8")
#print(message)

topic="processed"

producer= KafkaProducer(bootstrap_servers=['51.38.185.58:9092'])

producer.send(topic, message)

#Permet d'envoyer le message sans attendre que le buffer soit rempli
producer.flush()

consumer=KafkaConsumer(topic,
                        bootstrap_servers=['51.38.185.58:9092']
                        )

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic,
            message.partition, message.offset, message.key, message.value))


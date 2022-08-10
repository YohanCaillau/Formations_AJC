import joblib
from kafka import KafkaConsumer, TopicPartition
import json
import numpy as np

model = joblib.load('linear_regression.joblib')

#Tester le modèle
#print(type(model))
#X = [[100,2]]
#prediction = model.predict(X)
#print(prediction)

#Créer le consumer
consumer = KafkaConsumer(bootstrap_servers=['51.38.185.58:9092'],
                        value_deserializer=lambda v: json.loads(v.decode('utf-8')))

#Gérer les partitions
int_partition = 0
string_topic = "prediction_caillau"

Topic_partition = TopicPartition(string_topic, int_partition)

#Assigner une partition
consumer.assign([Topic_partition])

for message in consumer:
    print(message.value)
    result = np.array(message.value)
    prediction = model.predict(result)
    print(prediction)


from kafka import KafkaProducer

producer= KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])

topic="caillau"

message="salut, c'est yohan".encode("utf-8")
producer.send(topic, message)

#Permet d'envoyer le message sans attendre que le buffer soit rempli
producer.flush()
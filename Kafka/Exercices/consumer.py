from kafka import KafkaConsumer

topic='caillau'

consumer=KafkaConsumer(topic,
                        bootstrap_servers=['127.0.0.1:9092']
                        )

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic,
            message.partition, message.offset, message.key, message.value))
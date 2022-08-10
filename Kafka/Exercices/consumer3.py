from kafka import KafkaConsumer, TopicPartition
#from kafka.structs import TopicPartition

int_partition = 0
string_topic = "caillau"

Topic_partition = TopicPartition(string_topic, int_partition)


consumer=KafkaConsumer( bootstrap_servers=['51.38.185.58:9092'],
                        group_id="grp1",
                      )

consumer.assign([Topic_partition])
consumer.poll()
consumer.seek_to_end()


for message in consumer:
    print(message.value)

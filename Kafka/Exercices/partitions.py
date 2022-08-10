from kafka.admin import KafkaAdminClient, NewPartitions

admin_client = KafkaAdminClient(bootstrap_servers=['51.38.185.58:9092'])

partitions = NewPartitions(2)

topic = "prediction_caillau"

topic_partitions = {
                    topic: partitions
                   }

admin_client.create_partitions(topic_partitions)
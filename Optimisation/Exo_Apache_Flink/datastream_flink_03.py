#from pyflink.datastream.connectors import KafkaSource
from pyflink.datastream.connectors import FlinkKafkaConsumer
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common import WatermarkStrategy
from pyflink.common import SimpleStringSchema

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)
#scp ubuntu@40.121.110.217:/home/ubuntu/lce/flink-sql-connector.jar .
env.add_jars("C:/Users/yohan/OneDrive/Bureau/Formations/Cours/Optimisation/flink-sql-connector.jar")

MY_BOOTSTRAP_SERVERS = '127.0.0.1:9092'
TOPIC = "caillau"

"""
source = KafkaSource.builder() \
    .set_bootstrap_servers(MY_BOOTSTRAP_SERVERS) \
    .set_topics(input_topic) \
    .set_starting_offsets(KafkaOffsetsInitializer.latest()) \
    .set_value_only_deserializer(SimpleStringSchema()) \
    .build()
"""

kafka_consumer = FlinkKafkaConsumer(
    topics=TOPIC,
    deserialization_schema=SimpleStringSchema(),
    properties={'bootstrap.servers': MY_BOOTSTRAP_SERVERS})

ds = env.add_source(kafka_consumer)
ds.print()

env.execute()
#env.from_source(source, WatermarkStrategy.no_watermarks(), "Kafka Source")
import findspark
from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row
import pyspark.sql.functions as F
from pyspark.sql.functions import *
from pyspark.sql.types import *

from pyspark.streaming import StreamingContext

spark = SparkSession.builder.appName('mini_projet').master("local").getOrCreate()


findspark.init()
spark.sparkContext.setLogLevel("ERROR")

topic = "station_status"
bootstrap_server = "51.38.185.58:9092"
#bootstrap_server = "127.0.0.1:9092"

kafka_df = spark.readStream \
.format("kafka") \
.option("kafka.bootstrap.servers", bootstrap_server) \
.option("subscribe", topic) \
.option("includeHeaders", "true") \
.option("startingOffsets", "latest") \
.load()

#option("checkpointLocation", "/tmp/checkpoint")

#kafka_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
query = kafka_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)").writeStream.outputMode("complete").format("console").start()

query.awaitTermination()
#kafka_df.show(5)
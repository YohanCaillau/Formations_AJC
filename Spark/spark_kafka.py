from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from datetime import datetime
#from pyspark.streaming.kafka import KafkaUtils
import findspark

import os

SCALA_VERSION = '2.13'
SPARK_VERISON = '3.3.0'

# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.13:3.3.0 pyspark-shell'

#Initialisation de findspark
findspark.init()

#Création du SparkSession
spark = SparkSession.builder.appName("ProjetVelib")\
.config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.13:3.3.0")\
.master("local[2]")\
.getOrCreate()
#sc = SparkContext.getOrCreate()

df = spark.readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "51.38.185.58:9092")\
  .option("subscribe", "station_status")\
  .load()
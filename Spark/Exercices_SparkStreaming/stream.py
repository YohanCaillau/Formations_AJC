#Import
import time
import pyspark
import findspark
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

#Initialisation de findspark
findspark.init()

#Création du SparkSession
spark = SparkSession.builder.appName("Exemple Spark").getOrCreate()
sc = SparkContext.getOrCreate()

ssc = StreamingContext(sc, 1)

def process(time, rdd):
    rdd.saveAsTextFile("C:/Users/yohan/OneDrive/Bureau/Formations/Cours/Spark/Exercices_SparkStreaming/count.txt")

lines = ssc.textFileStream(directory = "C:/Users/yohan/OneDrive/Bureau/Formations/Cours/Spark/Exercices_SparkStreaming/test/")
counts = lines.flatMap(lambda line: line.split(" "))\
                  .map(lambda word: (word, 1))\
                  .reduceByKey(lambda x, y: x + y)
counts.pprint()
counts.foreachRDD(process)

import shutil
src=r"C:/Users/yohan/OneDrive/Bureau/Formations/Cours/Spark/Exercices_SparkStreaming/fichier.txt"
des=r"C:/Users/yohan/OneDrive/Bureau/Formations/Cours/Spark/Exercices_SparkStreaming/test/fichier.txt"
shutil.copy(src, des)

ssc.start()
#time.sleep(6)
ssc.stop(stopSparkContext=True, stopGraceFully=True)
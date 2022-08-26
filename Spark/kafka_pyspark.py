from pyspark.sql import SparkSession
from pyspark.sql.types import *
import findspark
import pyspark.sql.functions as psf
from pyspark.sql.functions import from_json, col, schema_of_json


if __name__ == "__main__":
    
    findspark.init()
    
    spark = (
        SparkSession.builder.appName("Kafka Pyspark Streaming Learning")
        .master("local[*]")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("ERROR")
    
    KAFKA_TOPIC_NAME = "station_status_maf"
    KAFKA_BOOTSTRAP_SERVER = "51.38.185.58:9092"
    
    df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVER)
        .option("subscribe", KAFKA_TOPIC_NAME)
        .option("startingOffsets", "latest")
        .load()
        .selectExpr("CAST(value as STRING)")
    )
    jschema = schema_of_json(col("value"))
    
    df2 = df.select(from_json(col("value") \
                    .cast("string"), schema= jschema).alias("parsed_value"))

    
    
    # schema = StructType([ \
    #     StructField("datasetid", StringType()), StructField("recordid", StringType()), \
    #     StructField("fields", StringType()), StructField("geometry", StringType()), \
    # ])  
    
    # def parse_data_from_kafka_message(sdf, schema):
    #     from pyspark.sql.functions import split
        

    #     col = split(sdf['value'], ',') #split attributes to nested array in one Column
    #     #now expand col to multiple top-level columns
        
    #     for idx, field in enumerate(schema): 
    #         sdf = sdf.withColumn(field.name, col.getItem(idx).cast(field.dataType))
    #     return sdf.select([field.name for field in schema])
    
    # test = parse_data_from_kafka_message(df, taxiRidesSchema)

    
    query = df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

    query.awaitTermination()

    #base_df = df.selectExpr("CAST(value as STRING)", "timestamp")
    #base_df.show()

    
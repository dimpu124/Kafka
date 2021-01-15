from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FlipkatMC").getOrCreate()

df = spark.read.json('C:\\Users\\sahus\\Desktop\\Flipkart\\Ostype')

df.show()


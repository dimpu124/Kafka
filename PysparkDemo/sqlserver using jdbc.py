from pyspark import SparkContext, SparkConf
from pyspark.sql import  SparkSession


spark = SparkSession.builder. \
    appName('DataFrame Demo'). \
    master('local'). \
    getOrCreate()


database = "Movies"
table = "dbo.Film"
user = "Dev"
password  = "iluvmyma"

jdbcDF = spark.read.format("jdbc") \
    .option("url", f"jdbc:sqlserver://IN2402580W1:1433;databaseName={database}") \
    .option("dbtable", "Movies") \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .load()

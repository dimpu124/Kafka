from pyspark.sql import  SparkSession


spark = SparkSession.builder. \
    appName('DataFrame Demo'). \
    master('local'). \
    getOrCreate()


import pyodbc
import pandas as pd
server_name = 'IN2402580W1'
database = "Movies"
table = "dbo.Film"
user = "Dev"
password  = "iluvmyma"

conn = pyodbc.connect('Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=yes;'%(server_name,database))
query = f"SELECT top 10 * FROM {table}"
pdf = pd.read_sql(query, conn)
sparkDF = spark.createDataFrame(pdf)
sparkDF.show()
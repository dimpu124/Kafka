from pyspark.sql import SparkSession
from pyspark import SparkFiles
from os import environ, listdir, path
import json

def start_spark(app_name = 'my_spark_app',master='local[*]',files=[],spark_config={}):
    spark_builder = (
        SparkSession
            .builder
            .master(master)
            .config("spark.driver.extraClassPath", "C:\\Users\\Saumya.Sahu\\Downloads\\Microsoft JDBC Driver 6.0 for SQL Server\\sqljdbc_6.0\\enu\\jre8\\sqljdbc42.jar")
            .appName(app_name))

    spark_files = ','.join(list(files))
    spark_builder.config('spark.files', spark_files)

    for key , val in spark_config.items():
        spark_builder.config(key,val)

    spark_sess = spark_builder.getOrCreate()

    spark_files_dir = SparkFiles.getRootDirectory()

    config_f = SparkFiles.get('Config/etl_config.json')

    config_files = [filename for filename in listdir(spark_files_dir)
                    if filename.endswith('config.json')]

    if config_files:
        path_to_config_file = path.join(spark_files_dir,config_files[0])
        with open(path_to_config_file,'r') as config_file:
            config_dict = json.load(config_file)
            print(config_file)
    else:
        config_dict = None

    return spark_sess,config_dict
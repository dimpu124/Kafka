from dependencies.spark import start_spark

def main():
    spark, config = start_spark(app_name='my_etl_job',files=['Config/etl_config.json'])
    path = config['file']['load']['path']

    data = extract(spark,path)
    transform_data = transform(data)
    load(transform_data)

def extract(spark,path):
    df = spark.read.json(path+'bot_devices.json')
    return df



def transform(data):
    df = data.selectExpr('id as device_id','name as device_name','date as created')
    return df



def load(transform_data):
    url = "jdbc:sqlserver://localhost:1433;databaseName=telemetry;integratedSecurity=true;"

    transform_data.write.mode("overwrite").format('jdbc') \
    .option("url",url) \
    .option("username","Dev") \
    .option("password","saumya124iter") \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .option("dbtable",'dm.dim_device') \
    .save()

    transform_data.write.mode("overwrite").format('csv')\
        .option('header',True)\
        .save("C:\\Users\\Saumya.Sahu\\OneDrive - EY\\Desktop\\SparkData\\data\\devicedata.csv")



if __name__ == '__main__':
    main()
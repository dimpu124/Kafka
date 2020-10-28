from pyspark import SparkConf,SparkContext

sc = SparkContext("local[2]")
sc.setLogLevel("DEBUG")
out = sc.textFile("C:\\SparkCourse\\DataSet\data-master\\retail_db\\orders")
out.map(lambda x : x.split(",")[1].split(" ")[0].replace("-","")).take(1)

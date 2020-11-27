from pyspark.sql import SparkSession,HiveContext
from os.path import join, abspath


warehouse_location = abspath('spark-warehouse')

spark = SparkSession \
    .builder \
    .appName("SalesReport") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()

salesOrder = spark.sql("""select Customerid,OrderQty,ProductID,UnitPrice,UnitPriceDiscount 
from salesorderheader sh 
join SalesOrderDetail so 
	on sh.salesorderid=so.salesorderid""")


salesOrder.createOrReplaceTempView("SalesOrderCust")


salesOrderGpByCid = spark.sql("select Customerid,(OrderQty*356.898)*(1-UnitPriceDiscount) as TotalSales ,ProductID from SalesOrderCust")
Customerdf = spark.sql(""" SELECT CustomerID,
      concat(coalesce(Title,''),' ',coalesce(FirstName,''),' ',coalesce(MiddleName,''),' ',coalesce(LastName,'')) as FullName
      ,CompanyName
      ,EmailAddress
      ,Phone
  FROM Customer""")

productdf = spark.sql("""select * from product""")

custsalesjoin = Customerdf.join(salesOrderGpByCid,"CustomerID")

custsalesprodjoin = custsalesjoin.join(productdf,"ProductID")

custSales = custsalesprodjoin.select("FullName","CompanyName","EmailAddress","name","TotalSales")

totalsalesperperson = custSales.groupby("FullName").sum("TotalSales")

totalsalesperperson = totalsalesperperson.withColumnRenamed("sum(TotalSales)","TotalSales")

totalsalesperproduct = custSales.groupby("name").sum("TotalSales")

totalsalesperproduct = totalsalesperproduct.withColumnRenamed("sum(TotalSales)","TotalSales")


totalsalesperproduct.write.mode("overwrite").saveAsTable("totalsalesperproduct")
totalsalesperperson.write.mode("overwrite").saveAsTable("totalsalesperperson")
custSales.write.mode("overwrite").saveAsTable("custSales")



from pyspark.sql import SparkSession # type: ignore
from pyspark.sql.functions import col, row # type: ignore


spark = SparkSession.builder.appName("spark_template").getOrCreate()

data = [(1,), (2,), (4,), (5,), (7,), (8,), (10,)]
df_numbers = spark.createDataFrame(data, ["Number"])

df_numbers.cache() # only in memory
df_numbers.persist() # different optionss

schema_json = ""
df = spark.read.schema(schema_json) \
            .options(header='True', multiline='True') \
            .format("csv") \
            .load("s3://e-commerce_bucket/data/daily/datetime/")

# option("header":"true")

df.write.parquet("path")
df.printSchema()
df.collect() # collects into a list and keep it in the driver
df.count() # do all these count of rows on the driver
df.show()
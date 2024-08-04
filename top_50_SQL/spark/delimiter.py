
# different delimiter in a file pyspark

from pyspark.sql import SparkSession # type: ignore
from pyspark.sql.functions import split, col  # type: ignore


spark = SparkSession.builder.appName("delimeter").getOrCreate()


data = ["1,Alice\t30|New York"]

df = spark.createDataFrame(data, "string")

split_col = split(df['value'], ',|\t|\|')


df = df.withColumn("id", split_col.getItem(0)) \
        .withColumn("name", split_col.getItem(1)) \
        .withColumn("age", split_col.getItem(2)) \
        .withColumn("city", split_col.getItem(3))


df = df.select("id", "name", "age", "city")


df.show()
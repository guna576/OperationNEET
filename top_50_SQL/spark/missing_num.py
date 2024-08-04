#find the missing value from the list

from pyspark.sql import SparkSession # type: ignore
from pyspark.sql.functions import col # type: ignore

spark = SparkSession.builder.appName("Find Missing Numbers").getOrCreate()

# Sample data
data = [(1,), (2,), (4,), (5,), (7,), (8,), (10,)]
df_given_numbers = spark.createDataFrame(data, ["Number"])

df_actual_numbers = spark.range(0,11).toDf("Number")

missing_numbers = df_actual_numbers.join(df_given_numbers,"Number", "left_anti")

missing_numbers.show()
# Generate a sequential number for each row within each group, ordered by date.

from pyspark.sql import SparkSession, Row # type: ignore
from pyspark.sql.functions import row_number, col # type: ignore
from pyspark.sql.window import Window # type: ignore

# Initialize Spark session
spark = SparkSession.builder.appName("RowNumberPerGroup").getOrCreate()

# Sample data
group_data = [
    Row(GroupID='A', Date='2023-01-01'),
    Row(GroupID='A', Date='2023-01-02'),
    Row(GroupID='B', Date='2023-01-01'),
    Row(GroupID='B', Date='2023-01-03')
]

# Create DataFrame
df_group = spark.createDataFrame(group_data)

df_group = spark.withColumn("Date", col("Date")).cast("date")

window_spec = Window.partitionBy("GroupID").orderBy("Date")

df_row_seq = df_group.withColumn("RowNum", row_number().over(window_spec))

df_row_seq.show()
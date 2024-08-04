# Find the count of unique visitors to a website per day.
# type: ignore
from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import countDistinct

# Initialize Spark session
spark = SparkSession.builder.appName("UniqueVisitorsPerDay").getOrCreate()

# Sample data
visitor_data = [Row(Date='2023-01-01', VisitorID=101),
                Row(Date='2023-01-01', VisitorID=102),
                Row(Date='2023-01-01', VisitorID=101),
                Row(Date='2023-01-02', VisitorID=103),
                Row(Date='2023-01-02', VisitorID=101)]

# Create DataFrame
df_visitors = spark.createDataFrame(visitor_data)

df_visitors = df_visitors.withColumn("Date", col("Date")).cast("date")

df_final = df_visitors.groupBy("Date").agg(countDistinct(col('VisitorID'))).alias("UniqueVisitorsCount")

df_final.show()

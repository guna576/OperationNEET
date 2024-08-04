# In a DataFrame df_sales with columns Date, ProductID, and QuantitySold, how would you calculate a 7-day rolling average of QuantitySold for each product?

from pyspark.sql import SparkSession # type: ignore
from pyspark.sql import Row # type: ignore
from pyspark.sql.window import Window # type: ignore
from pyspark.sql.functions import to_date, col, avg # type: ignore

# Initialize Spark session
spark = SparkSession.builder.appName("RollingAverageCalculation").getOrCreate()


# Sample data
data = [Row(Date='2023-01-01', ProductID=100, QuantitySold=10),
        Row(Date='2023-01-02', ProductID=100, QuantitySold=15),
        Row(Date='2023-01-03', ProductID=100, QuantitySold=20),
        Row(Date='2023-01-04', ProductID=100, QuantitySold=25),
        Row(Date='2023-01-05', ProductID=100, QuantitySold=30),
        Row(Date='2023-01-06', ProductID=100, QuantitySold=35),
        Row(Date='2023-01-07', ProductID=100, QuantitySold=40),
        Row(Date='2023-01-08', ProductID=100, QuantitySold=45)]

# Create DataFrame
df_sales = spark.createDataFrame(data)

# Convert Date string to Date type
df_sales = df_sales.withColumn("Date", to_date(col("Date")))

window = Window.partitionBy("ProductId").orderBy("Date").rowsBetween(-6,0)

rolling_avg = df_sales.withColumn("7_day_avg",avg("QuantitySold").over(window))

rolling_avg.show()
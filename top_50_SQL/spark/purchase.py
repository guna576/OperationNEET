# Determine the first purchase date for each user.


from pyspark.sql import SparkSession, Row # type: ignore
from pyspark.sql.functions import min, col # type: ignore

# Initialize Spark session
spark = SparkSession.builder.appName("FirstPurchaseDate").getOrCreate()

# Sample data
purchase_data = [
    Row(UserID=1, PurchaseDate='2023-01-05'),
    Row(UserID=1, PurchaseDate='2023-01-10'),
    Row(UserID=2, PurchaseDate='2023-01-03'),
    Row(UserID=3, PurchaseDate='2023-01-12')
]

# Create DataFrame
df_purchases = spark.createDataFrame(purchase_data)
df_purchases = df_purchases.withColumn("PurchaseDate", col("PurchaseDate").cast("date"))


df_first_purchases = df_purchases.groupBy("UserID").agg(min(col("PurchaseDate"))).alias("FirstPurchaseDate")

df_first_purchases.show()

# sql = """
# select 
# UserID,
# min(PurchaseDate) as first_purchase_date
# from Purchase
# group by UserID;
# """
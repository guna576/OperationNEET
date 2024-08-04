#Problem: Given a dataset of sales records, identify and replace all missing values in the 'amount' column with the average sales amount.


from pyspark.sql import SparkSession # type: ignore 
from pyspark.sql.functions import mean, col # type: ignore 


spark = SparkSession.builder.appName("Avg Sales Amount").getOrCreate()

data = [("1", 100), ("2", 150), ("3", None), ("4", 200), ("5", None)]

df_data = spark.createDataFrame(data, ["sale_id", "amount"])


avg_sales_amount = df_data.na.drop().agg(mean(col("amount"))).first()[0]

df_final_data = df_data.na.fill(avg_sales_amount)


df_final_data.show()


spark.stop()

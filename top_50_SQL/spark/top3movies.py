#find top 3 movie based on the rating

from pyspark.sql import SparkSession # type: ignore
from pyspark.sql.functions import avg # type: ignore

# Initialize Spark Session
spark = SparkSession.builder.appName("TopMovies").getOrCreate()

# Sample DataFrames
data_movies = [(1, "Movie A"), (2, "Movie B"), (3, "Movie C"), (4, "Movie D"), (5, "Movie E")]

data_ratings = [(1, 101, 4.5), (1, 102, 4.0), (2, 103, 5.0), 
                (2, 104, 3.5), (3, 105, 4.0), (3, 106, 4.0), 
                (4, 107, 3.0), (5, 108, 2.5), (5, 109, 3.0)]

columns_movies = ["MovieID", "MovieName"]
columns_ratings = ["MovieID", "UserID", "Rating"]

# Creating DataFrames
df_movies = spark.createDataFrame(data_movies, columns_movies)
df_ratings = spark.createDataFrame(data_ratings, columns_ratings)

df_avg_ratings = df_ratings.groupBy("Rating").alias("AvgRating")

df_final = df_movies.join(df_avg_ratings, "MovieID", "left_join").orderBy("AvgRating", Ascending = False).limit(3)

df_final.show()

"""
with AvgRating as (
    select *, Avg(Rating) as avg_rating
    from df_ratings
    group by MovieID
)

"""
"""
select 
dm.name
from data_movies dm join AvgRating dr 
on dm.MovieID = dr.MovieID
order by dr.avg_rating desc
limit 3 
"""
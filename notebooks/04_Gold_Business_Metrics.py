# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_reviews
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_review_sentiment_input

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_channels
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_purchase_channel_metrics

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_countries
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_country_review_metrics

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_products
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_product_review_volume

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_products
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_product_ratings

# COMMAND ----------

# MAGIC %md
# MAGIC Validating Gold Tables

# COMMAND ----------

gold_review_sentiment_input.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("dataengineer_practice.smartphone_sentiment_platform.gold_review_sentiment_input")

# COMMAND ----------

gold_purchase_channel_metrics.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("dataengineer_practice.smartphone_sentiment_platform.gold_purchase_channel_metrics")

# COMMAND ----------

gold_country_review_metrics.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("dataengineer_practice.smartphone_sentiment_platform.gold_country_review_metrics")

# COMMAND ----------

gold_product_review_volume.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("dataengineer_practice.smartphone_sentiment_platform.gold_product_review_volume")

# COMMAND ----------

gold_product_ratings.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("dataengineer_practice.smartphone_sentiment_platform.gold_product_ratings")

# COMMAND ----------

display(gold_review_sentiment_input)

# COMMAND ----------

gold_review_sentiment_input = (
    silver_reviews.select(
        "review_id",
        "product_id",
        "review_date",
        "rating",
        "review_text"
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC Preparing Customer reviews for downstream sentiment analysis

# COMMAND ----------

display(gold_purchase_channel_metrics)

# COMMAND ----------

gold_purchase_channel_metrics = (
    silver_reviews
    .join(
        silver_customers.select(
            "customer_id",
            "purchase_channel"
        ),
        "customer_id",
        "left"
    )
    .groupBy("purchase_channel")
    .agg(
        count("review_id").alias("total_reviews"),
        round(avg("rating"), 2).alias("average_rating")
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC #Purchase Channel Metrics

# COMMAND ----------

display(gold_country_review_metrics)

# COMMAND ----------

gold_country_review_metrics = (
    silver_reviews
    .join(
        silver_customers.select(
            "customer_id",
            "country"
        ),
        "customer_id",
        "left"
    )
    .groupBy("country")
    .agg(
        count("review_id").alias("total_reviews"),
        round(avg("rating"), 2).alias("average_rating")
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC #Country Review Metrics

# COMMAND ----------

display(
    gold_product_review_volume.orderBy(
        "total_reviews",
        ascending=False
    )
)

# COMMAND ----------

gold_product_review_volume = (
    gold_product_review_volume
    .join(
        silver_products.select(
            "product_id",
            "brand",
            "model_name"
        ),
        "product_id",
        "left"
    )
)

# COMMAND ----------

gold_product_review_volume = (
    silver_reviews
    .groupBy("product_id")
    .agg(
        count("review_id").alias("total_reviews")
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC #Product Review Volume Metrics

# COMMAND ----------

display(
    gold_product_ratings.orderBy(
        "average_rating",
        ascending=False
    )
)

# COMMAND ----------

from pyspark.sql.functions import avg, count, round

gold_product_ratings = (
    silver_reviews
    .groupBy("product_id")
    .agg(
        round(avg("rating"), 2).alias("average_rating"),
        count("review_id").alias("total_reviews")
    )
    .join(
        silver_products.select(
            "product_id",
            "brand",
            "model_name"
        ),
        "product_id",
        "left"
    )
)

# COMMAND ----------

from pyspark.sql.functions import avg, count, round

gold_product_ratings = ( silver_reviews
    .groupBy("product_id")
    .agg(
        round(avg("rating"), 2).alias("average_rating"),
        count("review_id").alias("total_reviews")
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC #Product Rating Metrics

# COMMAND ----------

silver_products = spark.table("dataengineer_practice.smartphone_sentiment_platform.silver_products")

silver_customers = spark.table("dataengineer_practice.smartphone_sentiment_platform.silver_customers")

silver_reviews = spark.table("dataengineer_practice.smartphone_sentiment_platform.silver_reviews")

# COMMAND ----------

# MAGIC %md
# MAGIC #Loading Silver Tables
# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_reviews
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.silver_reviews

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_customers
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.silver_customers

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_products
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.silver_products

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM dataengineer_practice.smartphone_sentiment_platform.silver_reviews;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM dataengineer_practice.smartphone_sentiment_platform.silver_customers;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM dataengineer_practice.smartphone_sentiment_platform.silver_products;

# COMMAND ----------

# MAGIC %md
# MAGIC #Validating Silver Tables

# COMMAND ----------

silver_reviews.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("dataengineer_practice.smartphone_sentiment_platform.silver_reviews")

# COMMAND ----------

silver_customers.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("dataengineer_practice.smartphone_sentiment_platform.silver_customers")

# COMMAND ----------

silver_products.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("dataengineer_practice.smartphone_sentiment_platform.silver_products")

# COMMAND ----------

silver_reviews = silver_reviews.filter(
    
    (col("rating").between(1, 5)) &
    (col("review_text").isNotNull())

)

# COMMAND ----------

# MAGIC %md
# MAGIC #Applying Data Quality rules

# COMMAND ----------

display(silver_reviews)

# COMMAND ----------

silver_reviews = reviews_df.dropDuplicates(["review_id"]) \
    .withColumn("rating", col("rating").cast("int"))

# COMMAND ----------

# MAGIC %md
# MAGIC ##Transforming Review Dataset

# COMMAND ----------

display(silver_customers)

# COMMAND ----------

silver_customers = customers_df.dropDuplicates(["customer_id"])

# COMMAND ----------

# MAGIC %md
# MAGIC ##Transforming Customer Dataset

# COMMAND ----------

display(silver_products)

# COMMAND ----------

from pyspark.sql.functions import col


silver_products = products_df.dropDuplicates(["product_id"]) \
    .withColumn("launch_year", col("launch_year").cast("int")) \
    .withColumn("storage_gb", col("storage_gb").cast("int")) \
    .withColumn("ram_gb", col("ram_gb").cast("int")) \
    .withColumn("price", col("price").cast("double"))

# COMMAND ----------

# MAGIC %md
# MAGIC ##Transforming Products Dataset

# COMMAND ----------

products_df = spark.table("dataengineer_practice.smartphone_sentiment_platform.bronze_products")

customers_df = spark.table("dataengineer_practice.smartphone_sentiment_platform.bronze_customers")

reviews_df = spark.table("dataengineer_practice.smartphone_sentiment_platform.bronze_reviews")

# COMMAND ----------

# MAGIC %md
# MAGIC
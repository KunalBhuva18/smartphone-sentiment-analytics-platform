# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT
# MAGIC     verified_purchase,
# MAGIC     COUNT(*) AS total_reviews
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_reviews
# MAGIC GROUP BY verified_purchase

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     rating,
# MAGIC     COUNT(*) AS total_reviews
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_reviews
# MAGIC GROUP BY rating
# MAGIC ORDER BY rating

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Data Quality Validation
# MAGIC
# MAGIC Validate business rules and domain values.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     COUNT(*) AS total_records,
# MAGIC     COUNT(DISTINCT review_id) AS distinct_reviews
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_reviews

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     COUNT(*) AS total_records,
# MAGIC     COUNT(DISTINCT customer_id) AS distinct_customers
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_customers

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     COUNT(*) AS total_records,
# MAGIC     COUNT(DISTINCT product_id) AS distinct_products
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_products

# COMMAND ----------

# MAGIC %md
# MAGIC ## Duplicate Record Validation
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     COUNT(*) AS total_records,
# MAGIC     COUNT(review_id) AS review_id_count,
# MAGIC     COUNT(customer_id) AS customer_id_count,
# MAGIC     COUNT(product_id) AS product_id_count,
# MAGIC     COUNT(review_text) AS review_text_count
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_reviews

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     COUNT(*) AS total_records,
# MAGIC     COUNT(customer_id) AS customer_id_count,
# MAGIC     COUNT(customer_name) AS customer_name_count,
# MAGIC     COUNT(country) AS country_count,
# MAGIC     COUNT(purchase_channel) AS purchase_channel_count
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_customers
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     COUNT(*) AS total_records,
# MAGIC     COUNT(product_id) AS product_id_count,
# MAGIC     COUNT(brand) AS brand_count,
# MAGIC     COUNT(model_name) AS model_name_count,
# MAGIC     COUNT(price) AS price_count
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_products
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Null Value Validation.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_reviews
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_reviews

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_customers
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_customers
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_products
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_products

# COMMAND ----------

# MAGIC %md
# MAGIC ## Record Count Validation
# MAGIC

# COMMAND ----------

products_df = spark.table("dataengineer_practice.smartphone_sentiment_platform.bronze_products")

customers_df = spark.table("dataengineer_practice.smartphone_sentiment_platform.bronze_customers")

reviews_df = spark.table("dataengineer_practice.smartphone_sentiment_platform.bronze_reviews")

# COMMAND ----------

# MAGIC %md
# MAGIC # Loading Bronze Tables
# MAGIC
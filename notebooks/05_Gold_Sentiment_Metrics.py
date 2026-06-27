# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC SELECT *
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_sentiment_summary
# MAGIC ORDER BY total_reviews DESC

# COMMAND ----------

# DBTITLE 1,Cell 1
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TABLE
# MAGIC dataengineer_practice.smartphone_sentiment_platform.gold_sentiment_summary
# MAGIC AS
# MAGIC
# MAGIC SELECT
# MAGIC     p.brand,
# MAGIC     p.model_name,
# MAGIC
# MAGIC     CAST(
# MAGIC         r.predicted_sentiment:response[0]
# MAGIC         AS STRING
# MAGIC     ) AS sentiment,
# MAGIC
# MAGIC     COUNT(*) AS total_reviews
# MAGIC
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_review_sentiment_predictions r
# MAGIC
# MAGIC JOIN dataengineer_practice.smartphone_sentiment_platform.silver_products p
# MAGIC ON r.product_id = p.product_id
# MAGIC
# MAGIC GROUP BY
# MAGIC     p.brand,
# MAGIC     p.model_name,
# MAGIC
# MAGIC     CAST(
# MAGIC         r.predicted_sentiment:response[0]
# MAGIC         AS STRING
# MAGIC     )
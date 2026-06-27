# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC SELECT *
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_review_sentiment_predictions
# MAGIC LIMIT 10

# COMMAND ----------

# DBTITLE 1,Cell 1
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE
# MAGIC dataengineer_practice.smartphone_sentiment_platform.gold_review_sentiment_predictions
# MAGIC AS
# MAGIC
# MAGIC SELECT
# MAGIC     review_id,
# MAGIC     product_id,
# MAGIC     review_date,
# MAGIC     rating,
# MAGIC     review_text,
# MAGIC
# MAGIC     ai_classify(
# MAGIC         review_text,
# MAGIC         '{"Positive": "Positive sentiment", "Neutral": "Neutral sentiment", "Negative": "Negative sentiment"}',
# MAGIC         map(
# MAGIC             'version','2.0',
# MAGIC             'multilabel','false'
# MAGIC         )
# MAGIC     ) AS predicted_sentiment
# MAGIC
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_review_sentiment_input
# MAGIC
# MAGIC WHERE review_text IS NOT NULL
# MAGIC
# MAGIC LIMIT 10000

# COMMAND ----------

# MAGIC %md
# MAGIC Agent Sentiment Prediction
# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC WITH brand_sentiment AS (
# MAGIC
# MAGIC SELECT
# MAGIC     brand,
# MAGIC     SUM(CASE WHEN sentiment='Positive' THEN total_reviews ELSE 0 END) AS positive_reviews,
# MAGIC     SUM(total_reviews) AS total_reviews
# MAGIC
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_sentiment_summary
# MAGIC
# MAGIC GROUP BY brand
# MAGIC
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     brand,
# MAGIC     ROUND((positive_reviews/total_reviews)*100,2) AS positive_sentiment_percentage
# MAGIC
# MAGIC FROM brand_sentiment
# MAGIC
# MAGIC ORDER BY positive_sentiment_percentage DESC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Business Question 5
# MAGIC
# MAGIC ### Which brands have the highest customer satisfaction rates?

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     sentiment,
# MAGIC     SUM(total_reviews) AS total_reviews
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_sentiment_summary
# MAGIC GROUP BY sentiment
# MAGIC ORDER BY total_reviews DESC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Business Question 4
# MAGIC
# MAGIC ### What is the overall customer sentiment across all smartphone products?

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     brand,
# MAGIC     sentiment,
# MAGIC     SUM(total_reviews) AS review_count
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_sentiment_summary
# MAGIC GROUP BY brand, sentiment
# MAGIC ORDER BY brand, review_count DESC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Business Question 3
# MAGIC
# MAGIC ### How does customer sentiment vary across brands?
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     brand,
# MAGIC     model_name,
# MAGIC     total_reviews AS positive_reviews
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_sentiment_summary
# MAGIC WHERE sentiment = 'Positive'
# MAGIC ORDER BY positive_reviews DESC
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %md
# MAGIC ## Business Question 2
# MAGIC
# MAGIC ### Which products have the highest customer satisfaction?
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     brand,
# MAGIC     model_name,
# MAGIC     total_reviews AS negative_reviews
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.gold_sentiment_summary
# MAGIC WHERE sentiment = 'Negative'
# MAGIC ORDER BY negative_reviews DESC
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %md
# MAGIC ## Business Question 1
# MAGIC
# MAGIC ###Which smartphone models should be prioritized for quality improvements?
# MAGIC
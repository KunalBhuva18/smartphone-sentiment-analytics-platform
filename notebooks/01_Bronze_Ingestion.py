# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_reviews
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_reviews

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_customers
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_customers

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_products
# MAGIC FROM dataengineer_practice.smartphone_sentiment_platform.bronze_products

# COMMAND ----------

# MAGIC %md
# MAGIC ## Validate Record Counts
# MAGIC

# COMMAND ----------

products_df.printSchema()

customers_df.printSchema()

reviews_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Validate Bronze Table Schemas

# COMMAND ----------

display(reviews_df)

# COMMAND ----------

display(customers_df)

# COMMAND ----------

display(products_df)

# COMMAND ----------

products_df = spark.table("dataengineer_practice.smartphone_sentiment_platform.bronze_products")

customers_df = spark.table("dataengineer_practice.smartphone_sentiment_platform.bronze_customers")

reviews_df = spark.table("dataengineer_practice.smartphone_sentiment_platform.bronze_reviews")

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC ## Load Bronze Delta Tables
# MAGIC
# MAGIC Raw CSV datasets were uploaded to Databricks and persisted as Delta Bronze tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS dataengineer_practice.smartphone_sentiment_platform;

# COMMAND ----------

# MAGIC %md
# MAGIC ##Bronze Layer Ingestion
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Ingest raw smartphone products, customers, and reviews datasets into Delta Bronze tables for downstream sentiment analytics and Agent Bricks workflows.
# MAGIC
# MAGIC ### Datasets
# MAGIC - products.csv
# MAGIC - customers.csv
# MAGIC - reviews.csv

# COMMAND ----------

# MAGIC %md
# MAGIC
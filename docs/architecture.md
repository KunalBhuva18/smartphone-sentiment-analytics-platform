# Smartphone Sentiment Analytics Platform Architecture

## Overview

The Smartphone Sentiment Analytics Platform was designed to simulate how a smartphone manufacturer or distributor could analyze customer feedback at scale.

The architecture follows the Medallion Architecture pattern (Bronze, Silver, and Gold) and integrates Generative AI capabilities available within Databricks.

The platform processes raw customer review data, generates business metrics, performs sentiment classification, and enables conversational analytics through Databricks Genie Space.

---

# High-Level Architecture

```text
Python + Faker
(Synthetic Data Generation)
                │
                ▼

        Raw CSV Files
(customers, products, reviews)
                │
                ▼

        Bronze Layer
(Raw Delta Tables Ingestion)
                │
                ▼

        Silver Layer
(Data Cleaning & Transformation)
                │
                ▼

         Gold Layer
(Business Metrics & KPIs)
                │
                ▼

 ┌───────────────────────────┐
 │ Executive Dashboard       │
 │ Sentiment Dashboard       │
 └───────────────────────────┘
                │
                ▼

AI Sentiment Classification
(Databricks ai_classify)
                │
                ▼

Gold Review Sentiment Table
                │
                ▼

      Databricks Genie Space
(Natural Language Analytics)
```

---

# Architecture Components

## 1. Synthetic Data Generation

Synthetic datasets were generated using Python, Pandas, and Faker to simulate a realistic smartphone retail environment.

Generated datasets include:

* Customers
* Products
* Reviews

The generated data is stored as CSV files and acts as the source system for the platform.

---

## 2. Bronze Layer

The Bronze layer ingests raw CSV files into Delta tables without applying any transformations.

### Objectives

* Preserve raw source data.
* Enable data lineage.
* Provide a reliable historical record.

### Bronze Tables

* bronze_customers
* bronze_products
* bronze_reviews

---

## 3. Silver Layer

The Silver layer performs data cleansing and standardization.

### Transformations Performed

* Null value handling.
* Duplicate removal.
* Schema standardization.
* Data validation checks.
* Data quality enforcement.

### Silver Tables

* silver_customers
* silver_products
* silver_reviews

---

## 4. Gold Layer

The Gold layer creates business-ready datasets that support analytics and reporting.

### Metrics Created

* Product review volumes.
* Product ratings.
* Country-level metrics.
* Purchase channel analysis.
* Customer sentiment metrics.

### Gold Tables

* gold_business_metrics
* gold_sentiment_summary
* gold_review_sentiment_predictions

---

## 5. AI Sentiment Classification

Databricks AI Functions were used to classify customer reviews into:

* Positive
* Neutral
* Negative

The `ai_classify()` function automatically analyzes review text and generates sentiment predictions.

The predictions are stored in:

```text
gold_review_sentiment_predictions
```

---

## 6. Dashboards

Two dashboards were created to provide business insights.

### Executive Dashboard

Provides:

* Total Reviews
* Total Customers
* Average Ratings
* Product Performance
* Country-Level Analysis

### Sentiment Dashboard

Provides:

* Sentiment Distribution
* Brand Sentiment Analysis
* Negative Review Analysis
* Positive Review Analysis

---

## 7. Conversational Analytics

Databricks Genie Space was integrated to enable natural language interaction with business data.

Example business questions include:

* Which smartphone models receive the most negative reviews?
* Which brands have the highest customer satisfaction?
* Which products should be prioritized for quality improvements?
* Compare customer sentiment across smartphone models.

This allows business users to generate insights without writing SQL queries.

---

# Key Design Decisions

* Implemented the Medallion Architecture to separate raw, cleansed, and business-ready datasets.
* Generated synthetic datasets to simulate a realistic business environment.
* Leveraged Databricks AI Functions to explore Generative AI use cases.
* Integrated Genie Space to provide conversational business intelligence capabilities.

---

# Future Enhancements

Potential future enhancements include:

* Auto Loader for real-time ingestion.
* Delta Live Tables (DLT) pipelines.
* Streaming data ingestion.
* Customer churn prediction models.
* Additional Generative AI use cases.

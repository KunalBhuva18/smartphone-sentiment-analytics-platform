# Smartphone Sentiment Analytics Platform

## Project Overview

I built this project to gain hands-on experience with Data Engineering concepts while exploring some of the Generative AI capabilities available within Databricks.

As I have been learning technologies such as PySpark, Delta Lake, Databricks, and SQL, I wanted to work on a project that would allow me to apply these concepts in a practical business scenario rather than only studying them theoretically.

The idea behind this project was to simulate how a smartphone manufacturer or distributor could analyze customer reviews to better understand customer satisfaction, identify product issues, and make data-driven decisions.

The platform processes raw review data using the Medallion Architecture (Bronze, Silver, and Gold layers), performs sentiment analysis using Databricks AI Functions, and allows business users to ask questions using natural language through Databricks Genie Space.

Project screenshots and dashboard outputs can be found in the `images/` folder.

---

## Business Problem

Smartphone manufacturers receive thousands of customer reviews across multiple products and sales channels. Reviewing this feedback manually can be time-consuming and makes it difficult to quickly identify customer concerns or product quality issues.

This project aims to answer business questions such as:

* Which smartphone models receive the most negative reviews?
* Which brands have the highest customer satisfaction?
* Which products should be prioritized for quality improvements?
* How does customer sentiment compare across competing products?

---

## Why I Built This Project

While learning Data Engineering, I realized that most tutorials focus on individual concepts separately. I wanted to build a project that combined multiple concepts into a single end-to-end solution.

Through this project, I was able to strengthen my understanding of:

* Data ingestion and transformation using PySpark.
* Implementing the Medallion Architecture.
* Working with Delta Lake in Databricks.
* Creating business metrics and dashboards.
* Applying Generative AI capabilities for sentiment analysis.
* Building conversational analytics using Databricks Genie Space.

---

## Technologies Used

* Python
* SQL
* PySpark
* Pandas
* Faker
* Databricks
* Delta Lake
* Databricks SQL
* Databricks Dashboards
* Databricks AI Functions (`ai_classify`)
* Databricks Genie Space
* Git & GitHub

---

## Dataset

Since publicly available datasets did not fully meet the project requirements, I generated my own synthetic dataset using Python, Pandas, and the Faker library.

### Dataset Summary

| Dataset   | Record Count |
| --------- | ------------ |
| Customers | 50,000       |
| Products  | 18           |
| Reviews   | 128,000      |

The dataset contains customer information, smartphone product details, and customer reviews across multiple brands.

---

## Solution Architecture

The project follows the Medallion Architecture pattern consisting of Bronze, Silver, and Gold layers.

### Bronze Layer

The Bronze layer is responsible for ingesting raw customer, product, and review data into Delta tables without modifying the source data.

**Notebook:** `01_Bronze_Ingestion.py`

### Silver Layer

The Silver layer performs data cleansing and transformation activities.

Transformations include:

* Data quality validation
* Null value handling
* Duplicate removal
* Schema standardization

**Notebook:** `03_Silver_Transformation.py`

### Gold Layer

The Gold layer contains business-ready datasets that support reporting, dashboards, and AI applications.

Business metrics created include:

* Product ratings
* Product review volumes
* Purchase channel analysis
* Country-level review analysis

**Notebook:** `04_Gold_Business_Metrics.py`

---

## Executive Dashboard

To provide business users with high-level insights, I created an executive dashboard in Databricks.

The dashboard includes:

* Total Reviews
* Total Customers
* Average Ratings
* Product Performance Analysis
* Review Distribution by Country
* Purchase Channel Analysis

Dashboard screenshots are available in the `images/` folder.

---

## AI-Powered Sentiment Analysis

One of the main goals of this project was to explore Generative AI capabilities within Databricks.

Using the `ai_classify()` function, customer reviews were automatically categorized into:

* Positive
* Neutral
* Negative

Examples:

| Review                                               | Predicted Sentiment |
| ---------------------------------------------------- | ------------------- |
| Outstanding performance for gaming and multitasking. | Positive            |
| Camera quality is fine but could be improved.        | Neutral             |
| Device experiences frequent app crashes.             | Negative            |

**Notebook:** `06_Agent_Sentiment_Predictions.py`

---

## Sentiment Intelligence Dashboard

After generating sentiment predictions, I created a second dashboard focused on customer sentiment across brands and products.

The dashboard helps answer questions such as:

* Which products receive the highest negative feedback?
* Which brands have the strongest customer sentiment?
* How is customer sentiment distributed across brands?

Dashboard screenshots are available in the `images/` folder.

---

## Business Questions Analysis

I also created a notebook focused on answering business questions from the perspective of smartphone manufacturers and distributors.

Examples include:

* Which smartphone models receive the most negative reviews?
* Which brands have the highest customer satisfaction?
* Which products should be prioritized for quality improvements?
* How does customer sentiment compare across products?

**Notebook:** `07_Business_Questions_Analysis.py`

---

## Conversational Analytics with Databricks Genie Space

To make the platform more business-friendly, I integrated Databricks Genie Space so that users can interact with the data using natural language instead of writing SQL queries.

Example questions:

* Which smartphone models receive the most negative reviews?
* Which brands have the highest customer satisfaction?
* Compare customer sentiment for Galaxy S25 and iPhone 16.
* Which products should be prioritized for quality improvements?

Sample Genie Space outputs and screenshots are available in the `images/` folder.

---

## Project Structure

```text
smartphone-sentiment-analytics-platform/
│
├── notebooks/
│   ├── 01_Bronze_Ingestion.py
│   ├── 02_Bronze_Validation.py
│   ├── 03_Silver_Transformation.py
│   ├── 04_Gold_Business_Metrics.py
│   ├── 05_Gold_Sentiment_Metrics.py
│   ├── 06_Agent_Sentiment_Predictions.py
│   └── 07_Business_Questions_Analysis.py
│
├── scripts/
├── data/
├── images/
├── docs/
└── README.md
```

---

## What I Learned

Working on this project helped me gain practical experience with:

* Building end-to-end data pipelines in Databricks.
* Performing data validation and transformation using PySpark.
* Designing Bronze, Silver, and Gold layers using the Medallion Architecture.
* Creating dashboards to present business insights.
* Using Databricks AI Functions for sentiment classification.
* Enabling business users to interact with data using natural language.

This project also helped me become more comfortable troubleshooting issues, debugging code, and understanding how different components work together in a modern data platform.

---

## Skills Demonstrated

* Data Engineering
* PySpark
* SQL
* Delta Lake
* Medallion Architecture
* Databricks
* Data Visualization
* Generative AI
* Databricks AI Functions
* Business Intelligence
* Conversational Analytics

---

## Future Improvements

As I continue learning, there are several enhancements that I would like to explore in future versions of this project:

* Implementing Auto Loader for real-time ingestion.
* Building Delta Live Tables (DLT) pipelines.
* Adding customer churn prediction models.
* Integrating data from external review platforms.
* Exploring additional Generative AI use cases.

---

## Author

**Kunal Bhuva**

Thank you for taking the time to review this project. Feedback and suggestions are always welcome.

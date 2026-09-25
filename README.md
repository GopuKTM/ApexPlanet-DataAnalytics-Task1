# ApexPlanet-DataAnalytics-Task1
# Task 1: Data Immersion & Wrangling

## Overview
This repository contains the data cleaning, profiling, feature transformation, and quality assessment pipeline for the ApexPlanet Data Analytics sales dataset.

---

## Data Quality Assessment Report

* **Missing Values Identified & Handled:**
  * `Age`: 20 missing values (~2.0%) — Imputed using the dataset median age (**41 years**).
  * `City`: 13 missing values (~1.3%) — Imputed as **`UNKNOWN`** to avoid losing valid transaction rows.
* **Duplicate Rows:** 0 exact full-row duplicates across all 1,000 records.
* **Calculation Verification:** Confirmed 100% mathematical accuracy for `Total_Sales = Quantity * Unit_Price` across all records.
* **Data Formatting:** `Order_Date` converted to **`DD-MM-YYYY`** format.
* **Feature Transformations:** Categorical **`Age_Group`** feature added to classify customer demographic brackets.

---

## Data Dictionary

| Column Name | Original Data Type | Cleaned Data Type | Business Meaning |
| :--- | :--- | :--- | :--- |
| **Order_ID** | String | String | Unique identifier for transaction orders |
| **Order_Date** | String | String / Date | Transaction date formatted as `DD-MM-YYYY` |
| **Customer_ID** | String | String | Unique identifier for customers |
| **Customer_Name** | String | String | Full name of the customer |
| **Age** | Float64 | Integer | Customer age (missing values imputed with median = 41) |
| **Gender** | String | String | Customer gender (`Male` / `Female`) |
| **City** | String | String | Delivery location city (missing values set to `UNKNOWN`) |
| **Product** | String | String | Name of the purchased item |
| **Category** | String | String | Category of the product |
| **Quantity** | Int64 | Int64 | Number of units purchased per order |
| **Unit_Price** | Float64 | Float64 | Cost per single unit |
| **Total_Sales** | Float64 | Float64 | Total monetary value of the order |
| **Age_Group** | Categorical | String / Categorical | Demographic bracket (`Gen Z (<25)`, `Young Adult (25-40)`, `Middle Aged (41-60)`, `Senior (>60)`) |

---

## Repository Files

* `clean_data.py`: Python script automating data quality fixes and dataset output.
* `Cleaned_Sales_Dataset.csv`: Analysis-ready output dataset containing 1,000 cleaned and feature-engineered records.


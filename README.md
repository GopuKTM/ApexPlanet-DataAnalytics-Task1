# ApexPlanet-DataAnalytics-Task1
# Task 1: Data Immersion & Wrangling

## Overview
This repository contains the data cleaning, profiling, and quality assessment pipeline for the ApexPlanet Data Analytics sales dataset.

---

## Data Quality Assessment Report

* **Missing Values Identified & Handled:**
  * `Age`: 20 missing values (~2.0%) — Imputed using the dataset median age (**41 years**).
  * `City`: 13 missing values (~1.3%) — Imputed as **`UNKNOWN`** to avoid losing valid transaction rows.
* **Duplicate Rows:** 0 exact full-row duplicates across all 1,000 records.
* **Calculation Verification:** Confirmed 100% mathematical accuracy for `Total_Sales = Quantity * Unit_Price` across all records.
* **Data Formatting:** `Order_Date` converted to native `datetime` format.

---

## Data Dictionary

| Column Name | Original Data Type | Cleaned Data Type | Business Meaning |
| :--- | :--- | :--- | :--- |
| **Order_ID** | String | String | Unique identifier for transaction orders |
| **Order_Date** | String | Datetime | Transaction date (`YYYY-MM-DD`) |
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

---

## Repository Files

* `clean_data.py`: Python script automating data quality fixes and dataset output.
* `Cleaned_Sales_Dataset.csv`: Analysis-ready output dataset containing 1,000 cleaned records.

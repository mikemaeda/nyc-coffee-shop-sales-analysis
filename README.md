# ☕ NYC Coffee Shop Sales: A Statistical Analysis

> **Project Documentation:** [PDF](./documentation.pdf)

## Project Overview
This project investigates consumer spending behavior across three New York City coffee shop locations: **Astoria, Hell's Kitchen, and Lower Manhattan**. Using a transactional dataset from January 2023, we analyze whether transaction value, pricing, and product category vary across these neighborhoods.

## Tech Stack & Methodology
* **Data Source:** "Coffee Shop Sales" dataset via Kaggle  
* **Statistical Methods:** One-Way and Two-Way ANOVA, Linear Regression, Chi-Square tests  
* **Core Objectives:**  
  - Determine if average spending differs by neighborhood  
  - Identify whether product preferences (Coffee vs. Tea, etc.) depend on store location  
  - Model the relationship between unit price and total transaction value  

## Key Insights

### 1. Consistency in Spending
Average transaction values do **not** differ significantly across locations:  
- Astoria: ~$4.62  
- Hell's Kitchen: ~$4.74  
- Lower Manhattan: ~$4.80  

Statistical tests confirm that customer spending behavior is consistent across all three locations.

### 2. Location-Specific Preferences
While spending is similar, product purchases differ significantly by location.  
Each store exhibits a unique purchasing pattern, which suggests inventory should be tailored to local preferences.

### 3. Price-Value Correlation
A linear regression showed that for every $1 increase in unit price, transaction value increases by approximately $1.16. About 43% of the variance in transaction value is explained by price, indicating that price is a strong driver of spending behavior.

## Business Recommendations
* **Tailored Inventory:** Stock products based on location-specific demand rather than a uniform approach.  
* **Optimized Staffing:** Schedule staff and promotions to align with afternoon peaks in transactions.

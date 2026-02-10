# nyc-coffee-shop-sales-analysis
Statistical analysis of NYC coffee shop sales using Excel and SQL to identify pricing trends, sales patterns, and operational insights.
# ☕ NYC Coffee Shop Sales: A Statistical Analysis

> **Please look at the full project documentation here:** [View PDF Presentation/Documentation](YOUR_LINK_HERE)

## 📋 Project Overview
[cite_start]This project performs an empirical investigation into consumer spending behavior across three New York City coffee shop locations: **Astoria, Hell's Kitchen, and Lower Manhattan**[cite: 12]. [cite_start]Using a transactional dataset of over 17,000 records from January 2023, the study evaluates whether location and time of day influence how much customers spend and what they choose to buy[cite: 13, 143, 144, 145].

## 🛠️ Tech Stack & Methodology
* [cite_start]**Data Source:** "Coffee Shop Sales" via Kaggle[cite: 24, 47].
* [cite_start]**Statistical Tools:** One-Way & Two-Way ANOVA, Chi-Square Test of Independence, and Simple Linear Regression[cite: 14].
* [cite_start]**Core Objectives:** * Determine if average transaction values differ by neighborhood[cite: 93].
    * [cite_start]Identify if product preferences are independent of store location[cite: 108, 202].
    * [cite_start]Model the relationship between unit price and total transaction value[cite: 112, 258].

## 🔍 Key Insights
### 1. The "Geography of Spending" (ANOVA)
[cite_start]Despite the different vibes of Astoria and Manhattan, the **average transaction value is remarkably consistent** across all locations (ranging from ~$4.62 to ~$4.80)[cite: 147, 149]. 
* [cite_start]**Result:** Failed to reject the Null Hypothesis ($p = 0.1426$)[cite: 151, 153]. [cite_start]Location does not significantly impact how much a customer spends per visit[cite: 154, 158].

### 2. Location-Based Preferences (Chi-Square)
[cite_start]While people spend the same *amount*, they do not buy the same *things*[cite: 15, 255].
* [cite_start]**Result:** Significant relationship ($p \approx 1.58 \times 10^{-25}$)[cite: 243, 247].
* [cite_start]**Finding:** Each store has a unique purchasing pattern (e.g., higher demand for specific teas or bakery items), meaning inventory should be tailored to the specific neighborhood[cite: 250, 256, 285].

### 3. Price vs. Value (Regression)
[cite_start]We found a positive linear relationship ($R^2 \approx 0.43$) between unit price and transaction value[cite: 258, 268, 274].
* [cite_start]**Finding:** For every $1 increase in unit price, the transaction value increases by approximately $1.16[cite: 271, 272].




## 💡 Business Recommendations
* [cite_start]**Micro-Level Inventory:** Retail managers should adapt product offerings to local store preferences identified in the Chi-Square analysis[cite: 37, 285, 288].
* [cite_start]**Afternoon Optimization:** Since transaction quantity and spending peak in the afternoon, staffing and promotional efforts should be concentrated in this window[cite: 177, 199, 282, 288].

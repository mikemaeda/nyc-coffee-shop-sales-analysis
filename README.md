# ☕ NYC Coffee Shop Sales: A Statistical Analysis

> **Please look at the documentation here:** [View Project Documentation (PDF)](./documentation .pdf)

## 📋 Project Overview
[cite_start]This project performs an empirical investigation into consumer spending behavior across three New York City coffee shop locations: **Astoria, Hell's Kitchen, and Lower Manhattan**[cite: 12]. [cite_start]Using a transactional dataset from January 2023, the study evaluates whether transaction value, pricing, and product category vary across these specific urban environments[cite: 13].

## 🛠️ Tech Stack & Methodology
* [cite_start]**Data Source:** "Coffee Shop Sales" dataset via Kaggle[cite: 47].
* [cite_start]**Statistical Models:** The analysis was conducted using One-Way and Two-Way ANOVA, Linear Regression, and Chi-Square tests of independence[cite: 14].
* [cite_start]**Core Objectives:** * To determine if average spending differs significantly by neighborhood[cite: 93].
    * [cite_start]To identify if product preferences (e.g., Coffee vs. Tea) are dependent on store location[cite: 108].
    * [cite_start]To model the relationship between unit price and total transaction value[cite: 258].

## 🔍 Key Insights

### 1. Consistency in Spending (One-Way ANOVA)
Despite the geographical differences, the analysis shows that average transaction values do not differ significantly across locations[cite: 15]. 
**Observation:** Astoria averaged ~$4.62, Hell's Kitchen ~$4.74, and Lower Manhattan ~$4.80[cite: 147].
Statistical Result:** With a p-value of 0.1426, we failed to reject the null hypothesis[cite: 153]. [cite_start]In real terms, customer spending behavior is consistent across all three locations[cite: 158].

### 2. Location-Specific Preferences (Chi-Square Test)
While people spend the same *amount*, they do not buy the same *products*. 
* [cite_start]**Statistical Result:** The Chi-Square test yielded a p-value of $1.58 \times 10^{-25}$[cite: 243]. 
* [cite_start]**Finding:** We reject the null hypothesis, meaning product category sales are highly dependent on the store location[cite: 249]. [cite_start]Each store exhibits a unique purchasing pattern[cite: 251].

### 3. Price-Value Correlation (Linear Regression)
[cite_start]We modeled the relationship between unit price and transaction value to understand spending drivers[cite: 258].
* [cite_start]**Equation:** $y = 1.1591x + 0.7664$[cite: 270].
* [cite_start]**Insight:** For every $1 increase in unit price, the transaction value increases by nearly $1.16[cite: 271]. [cite_start]The $R^2$ of 0.43 indicates that 43% of the transaction value is determined by the unit price[cite: 274].




## 💡 Business Recommendations
* [cite_start]**Tailored Inventory:** Retail strategy should consider location-specific product demand patterns rather than a uniform strategy[cite: 256].
* [cite_start]**Temporal Staffing:** Since transaction quantity peaks in the afternoon across all locations, staffing and marketing should be optimized for this window[cite: 282, 288].

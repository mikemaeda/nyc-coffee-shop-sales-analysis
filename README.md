# NYC Coffee Shop Sales Analysis

A reproducible Python analysis of transaction-level coffee shop sales across New York City locations. The project explores sales performance, customer spending patterns, product mix, and statistical relationships in the Coffee Shop Sales dataset.

## What This Analysis Covers

- Revenue and transaction trends by store location
- Average transaction value and unit price patterns
- Product category demand across neighborhoods
- Hourly sales activity and peak transaction periods
- Statistical testing for location, category, and price effects

## Repository Structure

```text
.
├── archive.zip                  # Source dataset, includes Coffee Shop Sales.xlsx
├── documentation.pdf            # Original written project documentation
├── requirements.txt             # Python dependencies
└── src/
    └── analyze_sales.py         # Reproducible analysis script
```

## Quick Start

```bash
python -m venv .venv
pip install -r requirements.txt
python src/analyze_sales.py --export-dir outputs
```

The script reads `archive.zip`, loads the Excel workbook inside it, cleans the transaction data, prints summary tables, runs statistical tests, and optionally exports CSV summary files to `outputs/`.

## Methods

The analysis uses:

- Descriptive statistics for revenue, transaction value, and volume
- One-way ANOVA to compare transaction value across store locations
- Chi-square testing to compare product category mix by location
- Linear regression to estimate the relationship between unit price and transaction value
- Two-way ANOVA for location and product category effects

## Key Takeaways

- Average transaction values are fairly consistent across the NYC locations.
- Product category demand varies by store, which supports location-specific inventory planning.
- Unit price has a measurable relationship with transaction value, but product mix and quantity also matter.
- Afternoon traffic patterns can help inform staffing, promotions, and stock planning.

## Data Source

Dataset: Coffee Shop Sales by Kerem Karayaz on Kaggle.

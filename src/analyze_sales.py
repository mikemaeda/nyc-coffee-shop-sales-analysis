from __future__ import annotations

import argparse
import io
import zipfile
from pathlib import Path
from typing import Optional, Tuple

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype, is_numeric_dtype
from scipy import stats

try:
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
except ImportError:  # pragma: no cover - handled at runtime for lighter installs
    sm = None
    ols = None

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARCHIVE = PROJECT_ROOT / "archive.zip"
REQUIRED_COLUMNS = {
    "transaction_id",
    "transaction_date",
    "transaction_time",
    "transaction_qty",
    "store_id",
    "store_location",
    "product_id",
    "unit_price",
    "product_category",
    "product_type",
    "product_detail",
}


def load_sales_data(archive_path: Path) -> pd.DataFrame:
    """Load and clean the Excel workbook stored inside the Kaggle archive."""
    if not archive_path.exists():
        raise FileNotFoundError(f"Could not find data archive: {archive_path}")

    with zipfile.ZipFile(archive_path) as archive:
        excel_files = [name for name in archive.namelist() if name.lower().endswith((".xlsx", ".xls"))]
        if not excel_files:
            raise FileNotFoundError("No Excel workbook was found inside the archive.")

        workbook_bytes = archive.read(excel_files[0])

    raw = pd.read_excel(io.BytesIO(workbook_bytes))
    return clean_sales_data(raw)


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize columns and add analysis-ready fields."""
    cleaned = df.copy()
    cleaned.columns = cleaned.columns.str.strip().str.lower()

    missing = sorted(REQUIRED_COLUMNS.difference(cleaned.columns))
    if missing:
        raise ValueError(f"Dataset is missing required columns: {', '.join(missing)}")

    cleaned["transaction_qty"] = pd.to_numeric(cleaned["transaction_qty"], errors="coerce")
    cleaned["unit_price"] = pd.to_numeric(cleaned["unit_price"], errors="coerce")
    cleaned = cleaned.dropna(subset=["transaction_qty", "unit_price", "store_location", "product_category"])

    cleaned["transaction_date"] = parse_excel_date(cleaned["transaction_date"])
    cleaned["hour"] = parse_excel_hour(cleaned["transaction_time"])
    cleaned["revenue"] = cleaned["transaction_qty"] * cleaned["unit_price"]

    return cleaned


def parse_excel_date(series: pd.Series) -> pd.Series:
    if is_datetime64_any_dtype(series):
        return pd.to_datetime(series, errors="coerce")
    if is_numeric_dtype(series):
        return pd.to_datetime(series, unit="D", origin="1899-12-30", errors="coerce")
    return pd.to_datetime(series, errors="coerce")


def parse_excel_hour(series: pd.Series) -> pd.Series:
    if is_numeric_dtype(series):
        seconds = pd.to_timedelta(series, unit="D").dt.total_seconds()
        return ((seconds // 3600) % 24).astype("Int64")

    parsed = pd.to_datetime(series.astype(str), errors="coerce")
    return parsed.dt.hour.astype("Int64")


def location_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("store_location")
        .agg(
            transactions=("transaction_id", "count"),
            units_sold=("transaction_qty", "sum"),
            revenue=("revenue", "sum"),
            avg_transaction_value=("revenue", "mean"),
            avg_unit_price=("unit_price", "mean"),
        )
        .sort_values("revenue", ascending=False)
        .round(2)
    )


def category_by_location(df: pd.DataFrame) -> pd.DataFrame:
    return pd.crosstab(df["store_location"], df["product_category"], values=df["revenue"], aggfunc="sum").fillna(0).round(2)


def hourly_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.dropna(subset=["hour"])
        .groupby("hour")
        .agg(transactions=("transaction_id", "count"), revenue=("revenue", "sum"))
        .sort_index()
        .round(2)
    )


def run_statistical_tests(df: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[pd.DataFrame]]:
    groups = [group["revenue"].to_numpy() for _, group in df.groupby("store_location")]
    anova_f, anova_p = stats.f_oneway(*groups)

    contingency = pd.crosstab(df["store_location"], df["product_category"])
    chi2, chi_p, chi_dof, _ = stats.chi2_contingency(contingency)

    regression = stats.linregress(df["unit_price"], df["revenue"])

    summary = pd.DataFrame(
        [
            {
                "test": "One-way ANOVA: revenue by location",
                "statistic": anova_f,
                "p_value": anova_p,
                "interpretation": "Location means differ" if anova_p < 0.05 else "No significant location mean difference",
            },
            {
                "test": "Chi-square: product category by location",
                "statistic": chi2,
                "p_value": chi_p,
                "interpretation": "Category mix varies by location" if chi_p < 0.05 else "No significant category-location relationship",
            },
            {
                "test": "Linear regression: revenue by unit price",
                "statistic": regression.slope,
                "p_value": regression.pvalue,
                "interpretation": f"Revenue changes about ${regression.slope:.2f} per $1 unit price increase",
            },
        ]
    ).round({"statistic": 4, "p_value": 6})

    two_way_anova = None
    if sm is not None and ols is not None:
        model = ols("revenue ~ C(store_location) + C(product_category) + C(store_location):C(product_category)", data=df).fit()
        two_way_anova = sm.stats.anova_lm(model, typ=2).round(4)

    return summary, two_way_anova


def print_table(title: str, table: pd.DataFrame) -> None:
    print(f"\n{title}")
    print("=" * len(title))
    print(table.to_string())


def export_tables(output_dir: Path, tables: dict[str, pd.DataFrame]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, table in tables.items():
        table.to_csv(output_dir / f"{name}.csv")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze NYC coffee shop sales data.")
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE, help="Path to archive.zip")
    parser.add_argument("--export-dir", type=Path, help="Optional directory for CSV summary outputs")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = load_sales_data(args.archive)

    tables = {
        "location_summary": location_summary(df),
        "category_by_location": category_by_location(df),
        "hourly_summary": hourly_summary(df),
    }
    test_summary, two_way_anova = run_statistical_tests(df)
    tables["statistical_tests"] = test_summary
    if two_way_anova is not None:
        tables["two_way_anova"] = two_way_anova

    print(f"Loaded {len(df):,} transactions from {args.archive.name}.")
    print_table("Location Summary", tables["location_summary"])
    print_table("Revenue by Product Category and Location", tables["category_by_location"])
    print_table("Hourly Summary", tables["hourly_summary"])
    print_table("Statistical Tests", test_summary)

    if two_way_anova is not None:
        print_table("Two-way ANOVA", two_way_anova)

    if args.export_dir:
        export_tables(args.export_dir, tables)
        print(f"\nExported summary files to {args.export_dir}")


if __name__ == "__main__":
    main()

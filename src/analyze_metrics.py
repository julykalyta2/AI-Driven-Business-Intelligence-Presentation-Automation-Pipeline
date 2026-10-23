
from pathlib import Path

import pandas as pd

# Find the project root based on this script's location.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "multifamily_operations.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
OUTPUT_FILE = OUTPUT_DIR / "monthly_kpis.csv"


def main():
    # Load the synthetic property data.
    df = pd.read_csv(INPUT_FILE)

    # Validate required fields before calculating metrics.
    required_columns = [
        "property_id",
        "property_name",
        "month",
        "units",
        "occupied_units",
        "rental_income",
        "other_income",
        "vacancy_loss",
        "operating_expenses",
        "budget_revenue",
        "budget_operating_expenses",
    ]

    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if df[required_columns].isnull().any().any():
        raise ValueError("Input data contains missing required values.")

    if (df["units"] <= 0).any():
        raise ValueError("Total units must be greater than zero.")

    if (
        (df["occupied_units"] < 0)
        | (df["occupied_units"] > df["units"])
    ).any():
        raise ValueError("Occupied units must be between zero and total units.")

    # Ensure monthly records are valid and consistently ordered.
    df["month"] = pd.to_datetime(df["month"], errors="raise")
    df = df.sort_values(["property_id", "month"]).copy()

    # Calculate operational and financial KPIs.
    df["occupancy_rate_pct"] = (
        df["occupied_units"] / df["units"] * 100
    ).round(2)

    df["gross_potential_income"] = (
        df["rental_income"] + df["other_income"]
    )

    df["effective_revenue"] = (
        df["gross_potential_income"] - df["vacancy_loss"]
    )

    df["net_operating_income"] = (
        df["effective_revenue"] - df["operating_expenses"]
    )

    df["revenue_variance"] = (
        df["effective_revenue"] - df["budget_revenue"]
    )

    df["expense_variance"] = (
        df["operating_expenses"] - df["budget_operating_expenses"]
    )

    df["noi_margin_pct"] = (
        df["net_operating_income"] / df["effective_revenue"] * 100
    ).round(2)

    # Flag periods that deserve management attention.
    df["occupancy_flag"] = df["occupancy_rate_pct"].apply(
        lambda value: "Review" if value < 95 else "On target"
    )

    df["revenue_flag"] = df["revenue_variance"].apply(
        lambda value: "Below budget" if value < 0 else "At/above budget"
    )

    # Save results for the next step in the reporting pipeline.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False, float_format="%.2f")

    print("Analysis completed.")
    print(f"Months analyzed: {len(df)}")
    print(f"Average occupancy: {df['occupancy_rate_pct'].mean():.2f}%")
    print(f"Total effective revenue: ${df['effective_revenue'].sum():,.2f}")
    print(f"Total operating expenses: ${df['operating_expenses'].sum():,.2f}")
    print(f"Total NOI: ${df['net_operating_income'].sum():,.2f}")
    print(f"Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

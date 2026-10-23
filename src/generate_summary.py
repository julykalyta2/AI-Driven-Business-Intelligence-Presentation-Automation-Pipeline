
from pathlib import Path
import pandas as pd

# Project paths
ROOT = Path(__file__).resolve().parent.parent
OUTPUTS = ROOT / "outputs"

# Load processed financial data
df = pd.read_csv(OUTPUTS / "monthly_kpis.csv")
df["month"] = pd.to_datetime(df["month"])
df = df.sort_values("month")

# Calculate financial performance
revenue = df["effective_revenue"].sum()
expenses = df["operating_expenses"].sum()
noi = df["net_operating_income"].sum()

occupancy = (
    df["occupied_units"].sum()
    / df["units"].sum() * 100
)

revenue_budget = df["budget_revenue"].sum()
expense_budget = df["budget_operating_expenses"].sum()

revenue_variance = revenue - revenue_budget
expense_variance = expenses - expense_budget

# Identify strongest and weakest months
best = df.loc[df["net_operating_income"].idxmax()]
worst = df.loc[df["net_operating_income"].idxmin()]

best_month = best["month"].strftime("%B")
worst_month = worst["month"].strftime("%B")

# Validate financial calculations
assert abs(noi - (revenue - expenses)) < 0.01

# Generate management observations
observations = []

if occupancy >= 95:
    observations.append(
        f"Average occupancy reached {occupancy:.2f}%, "
        "meeting the 95% operational target."
    )
else:
    observations.append(
        f"Average occupancy was {occupancy:.2f}%, "
        "below the 95% operational target."
    )

if revenue_variance >= 0:
    observations.append(
        f"Effective revenue exceeded budget by "
        f"${revenue_variance:,.0f}."
    )
else:
    observations.append(
        f"Effective revenue was below budget by "
        f"${abs(revenue_variance):,.0f}."
    )

if expense_variance > 0:
    observations.append(
        f"Operating expenses exceeded budget by "
        f"${expense_variance:,.0f}."
    )
else:
    observations.append(
        f"Operating expenses were at or below budget "
        f"by ${abs(expense_variance):,.0f}."
    )

# Create investor-ready summary
summary = f"""
PARKSIDE APARTMENTS
2026 ANNUAL INVESTOR PERFORMANCE SUMMARY

FINANCIAL OVERVIEW

Effective Revenue: ${revenue:,.0f}
Operating Expenses: ${expenses:,.0f}
Net Operating Income: ${noi:,.0f}
Average Occupancy: {occupancy:.2f}%

KEY PERFORMANCE INSIGHTS

1. {observations[0]}

2. {observations[1]}

3. {observations[2]}

4. The strongest NOI performance occurred in
   {best_month}, reaching
   ${best['net_operating_income']:,.0f}.

5. The weakest NOI performance occurred in
   {worst_month}, reaching
   ${worst['net_operating_income']:,.0f}.

MANAGEMENT RECOMMENDATIONS

- Review the drivers of revenue variance.
- Investigate months with lower occupancy.
- Monitor operating expense categories.
- Compare NOI trends with future periods.

DISCLAIMER

All financial data is synthetic.
This summary was generated using Python rules,
not a generative AI model.
"""

# Save the generated summary
OUTPUTS.mkdir(parents=True, exist_ok=True)

file_path = OUTPUTS / "management_summary.txt"
file_path.write_text(summary.strip(), encoding="utf-8")

print(summary)
print("\nSUMMARY GENERATED SUCCESSFULLY!")
print("Saved to:", file_path)

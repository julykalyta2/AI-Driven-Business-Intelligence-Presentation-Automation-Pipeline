
import os
import json
from pathlib import Path

import pandas as pd
from openai import OpenAI

ROOT = Path(__file__).resolve().parent.parent
OUTPUTS = ROOT / "outputs"

df = pd.read_csv(OUTPUTS / "monthly_kpis.csv")

metrics = {
    "property": "Parkside Apartments",
    "reporting_year": 2026,
    "average_occupancy_pct": round(
        df["occupied_units"].sum() /
        df["units"].sum() * 100, 2
    ),
    "effective_revenue": float(
        df["effective_revenue"].sum()
    ),
    "operating_expenses": float(
        df["operating_expenses"].sum()
    ),
    "net_operating_income": float(
        df["net_operating_income"].sum()
    ),
}

# Check financial consistency before sending data.
assert abs(
    metrics["net_operating_income"] -
    (metrics["effective_revenue"] -
     metrics["operating_expenses"])
) < 0.01

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.responses.create(
    model="gpt-4.1-mini",
    instructions=(
        "You are a multifamily real estate reporting analyst. "
        "Write a concise investor-ready management summary. "
        "Use only the provided metrics. "
        "Do not invent financial figures, causes, or forecasts. "
        "Clearly distinguish observations from recommendations. "
        "Return plain text with no Markdown."
    ),
    input=json.dumps(metrics)
)

summary = response.output_text.strip()

OUTPUTS.mkdir(parents=True, exist_ok=True)
(OUTPUTS / "ai_summary.txt").write_text(
    summary, encoding="utf-8"
)

print("AI summary generated successfully!")
print(summary)

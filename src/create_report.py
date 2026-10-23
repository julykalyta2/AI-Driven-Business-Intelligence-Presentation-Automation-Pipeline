
from pathlib import Path

import pandas as pd
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    Table, TableStyle, Image
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Paths work regardless of where the script is run.
ROOT = Path(__file__).resolve().parent.parent
OUTPUTS = ROOT / "outputs"

df = pd.read_csv(OUTPUTS / "monthly_kpis.csv")

revenue = df["effective_revenue"].sum()
expenses = df["operating_expenses"].sum()
noi = df["net_operating_income"].sum()
occupancy = df["occupied_units"].sum() / df["units"].sum() * 100

assert abs(noi - (revenue - expenses)) < 0.01

OUTPUTS.mkdir(parents=True, exist_ok=True)

doc = SimpleDocTemplate(
    str(OUTPUTS / "investor_report.pdf"),
    pagesize=(612, 792),
    leftMargin=45,
    rightMargin=45,
    topMargin=45,
    bottomMargin=45,
)

styles = getSampleStyleSheet()
story = [
    Paragraph("PARKSIDE APARTMENTS", styles["Title"]),
    Paragraph("2026 Annual Investor Performance Report",
              styles["Heading2"]),
    Paragraph("Synthetic Data | Portfolio Demonstration",
              styles["Normal"]),
    Spacer(1, 20),
]

summary = [
    ["Performance Metric", "2026 Result"],
    ["Average Occupancy", f"{occupancy:.2f}%"],
    ["Effective Revenue", f"${revenue:,.2f}"],
    ["Operating Expenses", f"${expenses:,.2f}"],
    ["Net Operating Income", f"${noi:,.2f}"],
]

table = Table(summary, colWidths=[260, 220])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0),
     colors.HexColor("#17324D")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1),
     [colors.white, colors.HexColor("#F0F4F8")]),
    ("GRID", (0, 0), (-1, -1),
     0.3, colors.lightgrey),
    ("TOPPADDING", (0, 0), (-1, -1), 10),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
]))

story.extend([
    table,
    Spacer(1, 24),
    Paragraph("Monthly Net Operating Income",
              styles["Heading2"]),
    Image(
        str(OUTPUTS / "monthly_noi.png"),
        width=7 * inch,
        height=3.2 * inch
    ),
    Spacer(1, 16),
])

lowest = df.loc[df["net_operating_income"].idxmin()]
highest = df.loc[df["net_operating_income"].idxmax()]

summary_text = (
    f"The property achieved average occupancy of "
    f"{occupancy:.2f}% during 2026. "
    f"Effective revenue totaled ${revenue:,.0f}, "
    f"with operating expenses of ${expenses:,.0f}, "
    f"resulting in NOI of ${noi:,.0f}. "
    f"The lowest monthly NOI occurred in "
    f"{pd.to_datetime(lowest['month']).strftime('%B')} "
    f"(${lowest['net_operating_income']:,.0f}), "
    f"while the highest occurred in "
    f"{pd.to_datetime(highest['month']).strftime('%B')} "
    f"(${highest['net_operating_income']:,.0f}). "
    "Management should review occupancy, revenue "
    "variances, and expenses for improvement opportunities."
)

story.extend([
    Paragraph("Management Performance Summary",
              styles["Heading2"]),
    Paragraph(summary_text, styles["BodyText"]),
    Spacer(1, 16),
    Paragraph(
        "Disclaimer: All data is synthetic. "
        "For portfolio demonstration only.",
        styles["Italic"]
    ),
])

doc.build(story)
print("Investor report generated successfully!")

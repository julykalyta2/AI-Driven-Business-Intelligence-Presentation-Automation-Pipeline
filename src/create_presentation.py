
from pathlib import Path
import pandas as pd
from pptx import Presentation
from pptx.util import Inches, Pt

BASE = Path(__file__).resolve().parent.parent
OUTPUT = BASE / "outputs"
OUTPUT.mkdir(exist_ok=True)

df = pd.read_csv(OUTPUT / "monthly_kpis.csv")

revenue = df["effective_revenue"].sum()
expenses = df["operating_expenses"].sum()
noi = revenue - expenses
occupancy = (df["occupied_units"].sum() / df["units"].sum()) * 100

# Handle occupancy stored as either a percentage or decimal
if occupancy <= 1:
    occupancy *= 100

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

def add_slide(title, lines):
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = title
    frame = slide.placeholders[1].text_frame
    frame.clear()
    for i, line in enumerate(lines):
        p = frame.paragraphs[0] if i == 0 else frame.add_paragraph()
        p.text = str(line)
        p.font.size = Pt(24)
    return slide

# Slide 1: Title
slide = prs.slides.add_slide(prs.slide_layouts[0])
slide.shapes.title.text = "Parkside Apartments"
slide.placeholders[1].text = (
    "2026 Investor Performance Presentation\n"
    "Synthetic Data | Automated Python Reporting"
)

# Slide 2: Financial KPIs
add_slide("2026 Financial Performance", [
    f"Effective Revenue: ${revenue:,.0f}",
    f"Operating Expenses: ${expenses:,.0f}",
    f"Net Operating Income: ${noi:,.0f}",
    f"Average Occupancy: {occupancy:.2f}%"
])

# Slide 3: NOI Chart
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.title.text = "Monthly Net Operating Income"
chart = OUTPUT / "monthly_noi.png"
if chart.exists():
    slide.shapes.add_picture(
        str(chart), Inches(1.0), Inches(1.3),
        width=Inches(11.3)
    )

# Slide 4: Management Summary
summary_path = OUTPUT / "management_summary.txt"
summary = summary_path.read_text(encoding="utf-8")
add_slide("Management Overview", [
    "Occupancy remained near the operational target.",
    "Revenue finished below budget.",
    "Operating expenses exceeded budget.",
    "Management should review variances and NOI trends."
])

# Slide 5: Recommendations
add_slide("Management Recommendations", [
    "Review revenue variance drivers.",
    "Investigate lower-occupancy months.",
    "Monitor operating expense categories.",
    "Compare monthly NOI with future periods."
])

# Slide 6: Methodology
add_slide("Automation & Methodology", [
    "Synthetic multifamily operations dataset",
    "Python and pandas financial analysis",
    "Automated matplotlib visualization",
    "Rule-based management commentary",
    "PowerPoint generated using python-pptx"
])

output_file = OUTPUT / "investor_presentation.pptx"
prs.save(output_file)
print(f"Presentation generated successfully: {output_file}")

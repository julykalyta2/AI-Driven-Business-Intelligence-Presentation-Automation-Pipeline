
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
OUTPUTS = ROOT / "outputs"

df = pd.read_csv(OUTPUTS / "monthly_kpis.csv")
df["month"] = pd.to_datetime(df["month"])
df = df.sort_values("month")

OUTPUTS.mkdir(parents=True, exist_ok=True)

# Generate NOI chart
fig, ax = plt.subplots(figsize=(11, 5))

ax.plot(
    df["month"],
    df["net_operating_income"],
    marker="o",
    linewidth=2
)

ax.set_title("Parkside Apartments | Monthly NOI")
ax.set_xlabel("Month")
ax.set_ylabel("Net Operating Income ($)")
ax.grid(alpha=0.3)

fig.autofmt_xdate()
fig.tight_layout()

fig.savefig(
    OUTPUTS / "monthly_noi.png",
    dpi=200
)

plt.close(fig)

print("NOI chart generated successfully!")

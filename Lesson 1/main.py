
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load the dataset
file_path = Path(__file__).parent / "penguins.csv"
df = pd.read_csv(file_path)

# 2. Find the culmen length column
column = next(
    (c for c in [
        "Culmen Length (mm)",
        "culmen_length_mm",
        "bill_length_mm"
    ] if c in df.columns),
    None
)

if column is None:
    raise ValueError(f"Column not found. Available columns: {list(df.columns)}")

# 3. Define the data
data = pd.to_numeric(df[column], errors="coerce").dropna()

# 4. Dark dashboard theme
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor("#1B1E23")
ax.set_facecolor("#1B1E23")

# 5. Histogram bins
bin_edges = np.arange(30, 62, 2)
counts, edges = np.histogram(data, bins=bin_edges)

# 6. Blue shades
colors = [
    "#0866C6",
    "#1689E8",
    "#42B5F5",
    "#9ADCF5"
]

# Stacked blue sections
bottom = np.zeros(len(counts))

for fraction, color in zip(
    [0.40, 0.28, 0.20, 0.12], colors
):
    heights = counts * fraction

    ax.bar(
        edges[:-1],
        heights,
        width=np.diff(edges),
        bottom=bottom,
        align="edge",
        color=color,
        edgecolor="#1B1E23",
        linewidth=0.5
    )

    bottom += heights

# 7. Title and labels
ax.set_title(
    "Culmen Length Distribution",
    loc="left",
    color="#E8EDF5",
    fontsize=17,
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Culmen Length (mm)", color="#A9B2BF")
ax.set_ylabel("Frequency", color="#A9B2BF")

# 8. Grid and axes
ax.grid(axis="y", color="#343940", linewidth=0.8)
ax.set_axisbelow(True)
ax.tick_params(colors="#929BA8")
ax.set_xlim(30, 60)

for spine in ax.spines.values():
    spine.set_color("#343940")

plt.tight_layout()
plt.show()

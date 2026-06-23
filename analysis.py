"""
Job Listings Data Analyser — Perth, WA
Author: Mansi Patel
Description: Exploratory data analysis of Perth tech job listings to identify
             in-demand skills, salary trends, and job market patterns.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from collections import Counter

# ── Style ──────────────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({"figure.dpi": 130, "font.family": "sans-serif"})
CHART_DIR = "charts/"

# ── 1. Load & Inspect ───────────────────────────────────────────────────────
print("=" * 55)
print("  STEP 1 — Loading data")
print("=" * 55)

df = pd.read_csv("data/perth_jobs.csv", parse_dates=["date_posted"])

print(f"\nDataset shape : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Columns       : {list(df.columns)}\n")
print("First 5 rows:")
print(df.head())

# ── 2. Data Cleaning ────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  STEP 2 — Cleaning data")
print("=" * 55)

print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nDuplicate rows: {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)
print(f"Rows after dedup: {len(df)}")

print(f"\nSalary range: ${df['salary_aud'].min():,} – ${df['salary_aud'].max():,}")
print(f"Average salary: ${df['salary_aud'].mean():,.0f}")

# ── 3. Top In-Demand Skills ─────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  STEP 3 — Most in-demand skills")
print("=" * 55)

all_skills = []
for skills_str in df["skills_required"].dropna():
    all_skills.extend([s.strip() for s in skills_str.split(",")])

skill_counts = Counter(all_skills)
top_skills = pd.DataFrame(skill_counts.most_common(15),
                           columns=["skill", "count"])
print(f"\nTop 10 skills:\n{top_skills.head(10).to_string(index=False)}")

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(top_skills["skill"][::-1], top_skills["count"][::-1],
               color=sns.color_palette("Blues_d", 15))
ax.set_xlabel("Number of job listings")
ax.set_title("Top 15 most in-demand skills — Perth tech jobs (2026)", fontweight="bold")
for bar in bars:
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
            str(int(bar.get_width())), va="center", fontsize=9)
plt.tight_layout()
plt.savefig(f"{CHART_DIR}01_top_skills.png")
plt.close()
print("  ✓ Saved charts/01_top_skills.png")

# ── 4. Salary by Job Title ──────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  STEP 4 — Salary by job title")
print("=" * 55)

salary_by_title = (df.groupby("job_title")["salary_aud"]
                     .median()
                     .sort_values(ascending=False))
print(f"\nMedian salary by title:\n{salary_by_title.to_string()}")

fig, ax = plt.subplots(figsize=(9, 6))
salary_by_title.plot(kind="barh", ax=ax, color=sns.color_palette("Greens_d", len(salary_by_title)))
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}k"))
ax.set_xlabel("Median salary (AUD)")
ax.set_title("Median salary by job title — Perth (2026)", fontweight="bold")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}02_salary_by_title.png")
plt.close()
print("  ✓ Saved charts/02_salary_by_title.png")

# ── 5. Job Types Distribution ───────────────────────────────────────────────
print("\n" + "=" * 55)
print("  STEP 5 — Job type distribution")
print("=" * 55)

job_type_counts = df["job_type"].value_counts()
print(f"\n{job_type_counts.to_string()}")

fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    job_type_counts, labels=job_type_counts.index,
    autopct="%1.1f%%", startangle=140,
    colors=sns.color_palette("Set2", len(job_type_counts))
)
ax.set_title("Job types in Perth tech listings (2026)", fontweight="bold")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}03_job_types.png")
plt.close()
print("  ✓ Saved charts/03_job_types.png")

# ── 6. Remote vs On-site ────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  STEP 6 — Remote / hybrid / on-site split")
print("=" * 55)

remote_counts = df["remote_option"].value_counts()
print(f"\n{remote_counts.to_string()}")

fig, ax = plt.subplots(figsize=(7, 4))
remote_counts.plot(kind="bar", ax=ax,
                   color=sns.color_palette("Purples_d", len(remote_counts)),
                   edgecolor="white")
ax.set_xlabel("")
ax.set_ylabel("Number of listings")
ax.set_title("Remote work options in Perth tech jobs (2026)", fontweight="bold")
ax.set_xticklabels(remote_counts.index, rotation=0)
plt.tight_layout()
plt.savefig(f"{CHART_DIR}04_remote_options.png")
plt.close()
print("  ✓ Saved charts/04_remote_options.png")

# ── 7. Salary vs Experience ─────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  STEP 7 — Salary vs experience (scatter)")
print("=" * 55)

fig, ax = plt.subplots(figsize=(8, 5))
scatter = ax.scatter(df["experience_years"], df["salary_aud"],
                     alpha=0.5, c=df["salary_aud"],
                     cmap="YlOrRd", edgecolors="none")
plt.colorbar(scatter, ax=ax, label="Salary (AUD)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}k"))
ax.set_xlabel("Years of experience")
ax.set_ylabel("Salary (AUD)")
ax.set_title("Salary vs experience — Perth tech jobs (2026)", fontweight="bold")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}05_salary_vs_experience.png")
plt.close()
print("  ✓ Saved charts/05_salary_vs_experience.png")

# ── 8. Key Insights Summary ─────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  STEP 8 — Key insights")
print("=" * 55)

top3_skills = [s for s, _ in skill_counts.most_common(3)]
top_paying = salary_by_title.idxmax()
most_common_type = df["job_type"].value_counts().idxmax()
part_time_pct = round(df[df["job_type"] == "Part-time"].shape[0] / len(df) * 100, 1)

print(f"""
  • Most in-demand skills  : {', '.join(top3_skills)}
  • Highest paying role    : {top_paying} (${salary_by_title.max():,.0f} median)
  • Most common job type   : {most_common_type}
  • Part-time listings     : {part_time_pct}% of all jobs
  • Avg salary (all roles) : ${df['salary_aud'].mean():,.0f}
""")

print("=" * 55)
print("  Analysis complete! Charts saved to charts/ folder.")
print("=" * 55)

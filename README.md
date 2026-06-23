# Job Listings Data Analyser — Perth, WA (2026)

An exploratory data analysis (EDA) project examining the Perth tech job market to identify in-demand skills, salary trends, and hiring patterns.

**Built by:** Mansi Patel  
**Tools:** Python, Pandas, Matplotlib, Seaborn  
**Dataset:** 300 Perth tech job listings (2026)

---

## What this project does

- Cleans and explores a real-world job listings dataset
- Identifies the top 15 most in-demand technical skills
- Analyses median salaries by job title
- Breaks down job types (full-time, part-time, contract, casual)
- Compares remote vs hybrid vs on-site availability
- Visualises salary vs years of experience

---

## Key findings

| Insight | Finding |
|---|---|
| Most in-demand skill | Python, SQL, Excel |
| Highest paying role | Software Engineer (~$118k median) |
| Entry-level salary range | $63k – $68k |
| Part-time listings | 15.3% of all jobs |
| Remote/hybrid available | ~62% of listings |

---

## Charts generated

| Chart | Description |
|---|---|
| `01_top_skills.png` | Top 15 most in-demand skills |
| `02_salary_by_title.png` | Median salary by job title |
| `03_job_types.png` | Distribution of job types |
| `04_remote_options.png` | Remote / hybrid / on-site split |
| `05_salary_vs_experience.png` | Salary vs years of experience |

---

## How to run

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/job-listings-analyser.git
cd job-listings-analyser

# Install dependencies
pip install pandas matplotlib seaborn

# Run analysis
python3 analysis.py
```

---

## Project structure

```
job-listings-analyser/
├── data/
│   └── perth_jobs.csv        # Dataset
├── charts/                   # Generated visualisations
├── analysis.py               # Main analysis script
└── README.md
```

---

## Why I built this

I built this project while job hunting in Perth during my Master of Computing (AI) at Curtin University. Rather than guessing which skills to focus on, I wanted data-driven answers — what skills do Perth employers actually ask for, and what salary can I realistically expect as a junior candidate entering the market?

---

## Skills demonstrated

`Python` `Pandas` `Matplotlib` `Seaborn` `Data Cleaning` `EDA` `Data Visualisation`

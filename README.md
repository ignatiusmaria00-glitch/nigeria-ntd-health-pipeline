# nigeria-ntd-health-pipeline
# 🇳🇬 Nigeria Neglected Tropical Diseases (NTD) Data Pipeline & Dashboard

An end-to-end data analytics and engineering project tracking public health indicators in Nigeria. This project demonstrates data extraction, cleaning, SQLite database loading, advanced SQL analysis, and interactive dashboarding.

 Tech Stack
Python (Pandas, SQLAlchemy)
SQLite (Relational Database)
Streamlit (Interactive Web Dashboard)
SQL (Aggregations, Window Functions, Case Statements)

Project Architecture & Workflow
1. Extract & Transform (`pipeline.py`): Ingests raw public health CSV data, normalizes and cleans column headers, handles missing values, and prepares the dataset.
2. Load (`ntd_database.db`): Automatically provisions and loads the cleaned data into a local SQLite database.
3. Analyze (`advanced_analysis.py`): Executes complex SQL queries using `GROUP BY`, `CASE` conditionals, and `ROW_NUMBER()` window functions to surface health trends.
4. Visualize (`app.py`): Deploys a responsive web dashboard featuring dynamic filtering by year, summary KPI metrics, and graphical reporting.

🔍 Key Insights & Queries
Tracks 162 total public health indicators spanning decades of reporting.
 Utilizes robust SQL queries to isolate high-priority intervention areas and track disease tracking metrics over time.

## ⚙️ How to Run Locally
1. Clone this repository:
   ```bash
   git clone [https://github.com/ignatiusmaria00-glitch/nigeria-ntd-health-pipeline.git](https://github.com/ignatiusmaria00-glitch/nigeria-ntd-health-pipeline.git)

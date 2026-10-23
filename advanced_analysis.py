import pandas as pd
from sqlalchemy import create_engine

# 1. Connect to your database
engine = create_engine("sqlite:///ntd_database.db")

print("--- 1. GROUP BY & AGGREGATION: Average value per indicator ---")
query_agg = """
SELECT gho_display, COUNT(*) as total_records, ROUND(AVG(numeric), 2) as avg_value
FROM nga_ntd_indicators
GROUP BY gho_display
ORDER BY total_records DESC
LIMIT 5;
"""
print(pd.read_sql(query_agg, con=engine))
print("\n" + "="*50 + "\n")


print("--- 2. CONDITIONAL CASE STATEMENT: Categorizing data levels ---")
# This groups numeric values into categories (High, Moderate, Low, or Missing)
query_case = """
SELECT gho_display, year_display, numeric,
       CASE 
           WHEN numeric > 50 THEN 'High'
           WHEN numeric BETWEEN 10 AND 50 THEN 'Moderate'
           WHEN numeric < 10 THEN 'Low'
           ELSE 'Unclassified / Missing'
       END as value_category
FROM nga_ntd_indicators
LIMIT 5;
"""
print(pd.read_sql(query_case, con=engine))
print("\n" + "="*50 + "\n")


print("--- 3. WINDOW FUNCTION: Ranking indicators by year ---")
# Using a window function to rank rows based on numeric values within each year
query_window = """
SELECT year_display, gho_display, numeric,
       ROW_NUMBER() OVER(PARTITION BY year_display ORDER BY numeric DESC) as rank_in_year
FROM nga_ntd_indicators
WHERE numeric IS NOT NULL
LIMIT 10;
"""
print(pd.read_sql(query_window, con=engine))
print("\n" + "="*50 + "\n")


print("--- 4. FILTERING & SUBQUERIES: Above average indicators ---")
# Finding records where the numeric value is higher than the overall database average
query_subquery = """
SELECT gho_display, year_display, numeric
FROM nga_ntd_indicators
WHERE numeric > (SELECT AVG(numeric) FROM nga_ntd_indicators WHERE numeric IS NOT NULL)
LIMIT 5;
"""
print(pd.read_sql(query_subquery, con=engine))
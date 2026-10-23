import pandas as pd
from sqlalchemy import create_engine

# 1. EXTRACT: Read from your CSV file in Downloads
csv_filename = "neglected_tropical_diseases_indicators_nga.csv"
print(f"Reading {csv_filename}...")
df = pd.read_csv(csv_filename)

# 2. TRANSFORM: Clean column names so they are safe for SQL
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[()]", "", regex=True)
df = df.dropna(how="all")

print(f"Data cleaned successfully. Total rows to load: {len(df)}")

# 3. LOAD: Write into a local SQLite database file named 'ntd_database.db'
engine = create_engine("sqlite:///ntd_database.db")
df.to_sql("nga_ntd_indicators", con=engine, if_exists="replace", index=False)

print("Pipeline executed successfully! Data loaded into SQLite database 'ntd_database.db'.")
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Page configuration
st.set_page_config(page_title="Nigeria NTD Health Dashboard", layout="wide")

# Title and description
st.title("🇳🇬 Nigeria Neglected Tropical Diseases (NTD) Analytics Dashboard")
st.markdown("This dashboard showcases public health indicator trends processed via an automated SQLite data pipeline.")

# Connect to database
engine = create_engine("sqlite:///ntd_database.db")

@st.cache_data
def load_data():
    query = "SELECT * FROM nga_ntd_indicators"
    return pd.read_sql(query, con=engine)

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Options")
selected_year = st.sidebar.selectbox("Select Year", sorted(df['year_display'].dropna().unique(), reverse=True))

# Filter dataframe by year
filtered_df = df[df['year_display'] == selected_year]

# Main Metrics Layout
col1, col2, col3 = st.columns(3)
col1.metric("Total Indicators Tracked", len(df))
col2.metric("Year Selected", selected_year)
col3.metric("Records for this Year", len(filtered_df))

st.markdown("---")

# Display filtered data table
st.subheader(f"Health Indicators for {selected_year}")
st.dataframe(filtered_df[['gho_display', 'numeric']].dropna(), use_container_width=True)

# Simple Bar Chart of top numeric values for the selected year
st.subheader("Top Indicator Values")
chart_data = filtered_df[['gho_display', 'numeric']].dropna().set_index('gho_display')
st.bar_chart(chart_data)
import os
from pathlib import Path
from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
import duckdb
con = duckdb.connect('./duckdb.db')

st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
"# Cannabis Analytes"
con = duckdb.connect('./duckdb.db')
tables = con.sql("SELECT table_name FROM information_schema.tables WHERE table_schema = 'main'").df()["table_name"].tolist()

selected_table = st.selectbox("Tables:", tables)
df = con.execute(f"SELECT * FROM {selected_table} LIMIT 100").df()

# Convert problematic columns to strings to avoid conversion errors
for col in df.columns:
    if df[col].dtype == 'object':
        try:
            df[col] = df[col].astype(float)
        except ValueError:
            df[col] = df[col].astype(str)

with st.expander("Raw Data", expanded=False):
    st.write(df)

pyg_app = StreamlitRenderer(df)
pyg_app.explorer()
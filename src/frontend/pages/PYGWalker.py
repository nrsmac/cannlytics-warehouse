"""Display duckdb data using pygwalker."""

import polars as pl
import streamlit as st
from duckdb_tools import execute_sql_polars, get_tables
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(layout="wide")
st.write("# Cannabis Test Data Warehouse")
st.write("## PygWalker")

tables = get_tables()
table = st.selectbox("Select Table", tables)
sample_size = st.number_input("Sample Size", value=1000, min_value=1, max_value=100000)
if table:
    df = execute_sql_polars(f"SELECT * FROM {table} USING SAMPLE {sample_size}")
    pyg_app = StreamlitRenderer(df)

    pyg_app.explorer()
    pyg_app.explorer()

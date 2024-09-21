import streamlit as st
from duckdb_tools import execute_sql, get_tables

st.set_page_config(page_title="cannyltics", layout="wide")
st.write("# Cannabis Test Data Warehouse")
st.write("## DuckDB SQL")
tables = get_tables()

sql = st.text_area("Enter DuckDB SQL:")

if st.button("Execute"):
    with st.spinner("Executing..."):
        df = execute_sql(sql)
        if df is not None:
            num_rows, num_cols = df.shape
            st.write(f"{num_rows} rows and {num_cols} columns")
            st.dataframe(df)
        st.write("SQL Executed. No results to display.")

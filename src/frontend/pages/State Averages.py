import duckdb
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from duckdb_tools import execute_sql, get_tables

st.set_page_config(page_title="cannyltics", layout="wide")
st.write("# Cannabis Test Data Warehouse")
st.write("## State Averages")


@st.cache_data()
def get_states() -> pd.DataFrame:
    """Get list of states in DuckDB."""
    with duckdb.connect("./duckdb.db") as con:
        duckdb_states = (
            con.sql("SELECT DISTINCT state FROM state_averages").df()["state"].tolist()
        )
    return duckdb_states


@st.cache_data()
def collect_state_averages_unpivot(states):
    state_dfs = [
        execute_sql(
            f"""
            SELECT * EXCLUDE state FROM (UNPIVOT (FROM state_averages WHERE state = '{state}')
            ON COLUMNS (* EXCLUDE state)
            INTO NAME 'Test' VALUE "{state} Average")"""
        )
        for state in states
    ]
    # Merge all on the 'Test' column, ensuring no duplicate columns
    _df = pd.concat(state_dfs, axis=1)
    # Remove duplicate columns

    _df = _df.loc[:, ~_df.columns.duplicated()]
    return _df


@st.cache_data()
def collect_state_average_data(states):
    states_str = ", ".join([f"'{state}'" for state in states])
    _df = execute_sql(
        f"""
        SELECT * FROM state_averages WHERE state IN ({states_str})"""
    )
    # Merge all on the 'Test' column, ensuring no duplicate columns
    return _df


all_states = get_states()
select_all = st.checkbox("Select All States", False)
if select_all:
    states = all_states
    disabled = True
else:
    states = st.multiselect("Select States:", all_states, key="select_states")
    disabled = False

# Disable the multiselect if the checkbox is clicked
st.multiselect(
    "Select States:", all_states, disabled=select_all, key="select_states_disabled"
)

if states:
    averages_df = collect_state_average_data(states)
    tests = averages_df.columns[1:]
    compare_df = collect_state_averages_unpivot(states)

    # Display the merged DataFrame
    st.write(compare_df)
    print(compare_df)

    selected_tests = st.multiselect("Select Test:", tests)
    # Plot the selected tests as bar charts
    for test in selected_tests:
        fig = go.Figure()
        for state in states:
            state_data = averages_df[averages_df["state"] == state]
            fig.add_trace(
                go.Bar(
                    x=state_data["state"],
                    y=state_data[test],
                    name=state,
                )
            )
        fig.update_layout(
            title=f"{test} by State",
            barmode="group",
            xaxis_title="State",
            yaxis_title=test,
        )
        st.plotly_chart(fig)

    with st.expander("Show Data"):
        st.dataframe(averages_df)

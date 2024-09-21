import duckdb
import pandas as pd
import polars as pl


def get_tables() -> pd.DataFrame:
    """Get list of tables in DuckDB."""
    with duckdb.connect("./duckdb.db") as con:
        duckdb_tables = con.sql("SHOW TABLES").df()["name"].tolist()
    return duckdb_tables


def execute_sql(sql: str) -> pd.DataFrame:
    """Execute SQL against duckdb and return DataFrame."""
    with duckdb.connect("./duckdb.db") as con:
        _df = con.sql(sql).df()
    return _df


def execute_sql_polars(sql: str) -> pl.DataFrame:
    """Execute SQL against duckdb and return DataFrame."""
    with duckdb.connect("./duckdb.db") as con:
        _df = con.sql(sql).pl()
    return _df

import duckdb
import pandas as pd


def get_tables() -> pd.DataFrame:
    """Get list of tables in DuckDB."""
    with duckdb.connect("./duckdb.db") as con:
        duckdb_tables = (
            con.sql(
                "SELECT table_name FROM information_schema.tables WHERE table_schema = 'main'"
            )
            .df()["table_name"]
            .tolist()
        )
    return duckdb_tables


def execute_sql(sql: str) -> pd.DataFrame:
    """Execute SQL against duckdb and return DataFrame."""
    with duckdb.connect("./duckdb.db") as con:
        _df = con.sql(sql).df()
    return _df

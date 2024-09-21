"""Export materialized views to CSV files."""
import os
from pathlib import Path

import duckdb

# Connect to the database
con = duckdb.connect('duckdb.db')

# Get the list of materialized views from models defined in ./src/transformations/materialized

materialized_models_path = Path(os.getcwd(), 'src/transformations/models/materialized')
materialized_views = [
    file.replace('.sql', '') for file in os.listdir(materialized_models_path)
]

for view in materialized_views:
    con.sql(f"COPY {view} TO 'data/materialized/{view}.csv' (HEADER, DELIMITER ',')")    con.sql(f"COPY {view} TO 'data/materialized/{view}.csv' (HEADER, DELIMITER ',')")
import duckdb
import os
from pathlib import Path


def load_excel_dataset_from_folder(con, folder_path, dataset):
    """Load all Excel files from a folder into a DuckDB database in a dataset schema."""
    print(f"Loading dataset {dataset} from {folder_path}")
    for filename in os.listdir(Path(os.getcwd(),folder_path)):
        if filename.endswith('.xlsx'):  # Check for Excel files
            file_path = os.path.join(folder_path, filename)
            # Load the Excel file into DuckDB
            table_name = filename.split('.')[0]
            con.sql(f"CREATE SCHEMA IF NOT EXISTS '{dataset}';")
            print(f"Loading {table_name} from {file_path}")
            sql = f"""
                CREATE TABLE IF NOT EXISTS "{dataset}"."{table_name}" AS
                SELECT *, '{table_name.split('-')[0].upper()}' AS state FROM st_read('{file_path}')
            """
            con.execute(sql)


def main():
    raw_data_path = './data/raw'
    datasets = ['test-results']
    con = duckdb.connect('./duckdb.db')
    con.sql("PRAGMA threads=4")
    con.sql("PRAGMA enable_optimizer")
    con.sql("SET memory_limit = '1GB'")
    con.sql("PRAGMA enable_print_progress_bar")
    con.sql("PRAGMA enable_progress_bar")
    con.sql("INSTALL SPATIAL;")
    con.sql("LOAD SPATIAL;")
    for dataset in datasets:
        load_excel_dataset_from_folder(con, Path(raw_data_path,dataset), dataset)


    con.close()

if __name__ == '__main__':
    main()
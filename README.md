# Cannalytics Data Warehouse
A proof-of-concept minimal data warehouse for cannabis test data powered by DuckDB + dbt.

## Features
- Data Transformation Pipelines defined in SQL
- Full data lineage from raw to materialized views (dbt docs)
- Declarative schema tests (dbt)
- Lightning fast aggregations and transformations with DuckDB

## Instructions
### Prerequisites:
- Make
- Poetry
- Docker (Optional)

```bash
poetry install  # Install dependencies in a virtual environment (by default Poetry config)
make download-data  # Download excel files from Cannlytics
make load-data  # Load raw data into DuckDB (can take a while, may use up to 5GiB of disk)
make transform-data  # Use dbt to run transformations inside DuckDB.
make run-dev  # Launch streamlit application
```

### Viewing Data Asset Lineage + Docs
```bash
make docs
```
Navigate to localhost:8080, and click on the blue dot in the bottom-right corner to see lineage.

## Future Directions
- Transform Orchestration (Dagster)
- Parquet storage
- Visualization/BI Platform (Superset)
- Automated ingestion from APIs/source data
- Live streaming logs from test sites
- Postgres or other data warehouse for high availability
- Iceberg Tables supporting schema evolution and versioning
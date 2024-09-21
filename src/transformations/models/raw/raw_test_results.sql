{{ config(materialized='view') }}

WITH raw_table as (
    {{ combine_tables_from_schema('test-results') }} 
)
SELECT * FROM raw_table
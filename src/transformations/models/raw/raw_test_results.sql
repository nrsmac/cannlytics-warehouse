{{ config(materialized='view') }}

{{ combine_tables_from_schema('test-results') }}

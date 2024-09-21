-- Replace all values equalling '-' with NULL
{% set test_cols = dbt_utils.get_column_values(table=ref('tests'), column='test_name') %}
WITH clean_table as (
    SELECT
        state,
        -- Try to cast the value to a number, if it fails, cast it to VARCHAR
        {% for test in test_cols %}
        "{{ test }}",
        {% endfor %}
    FROM {{ ref('raw_test_results') }}
)
SELECT * FROM clean_table
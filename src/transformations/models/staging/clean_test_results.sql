-- Replace all values equalling '-' with NULL
{% set test_cols = dbt_utils.get_column_values(table=ref('tests'), column='test_name') %}
WITH clean_table as (
    SELECT
        state,
        {% for test in test_cols %}
        "{{ test }}",
        {% endfor %}
    FROM {{ ref('raw_test_results') }}
)
SELECT * FROM clean_table
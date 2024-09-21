{% set test_cols = dbt_utils.get_column_values(table=ref('tests'), column='test_name') %}
WITH filtered AS (
    SELECT
        state,
        {% for test in test_cols %}
        "{{ test }}",
        {% endfor %}
    FROM {{ ref('clean_test_results') }} 
)

SELECT * FROM filtered
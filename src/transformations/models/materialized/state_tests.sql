{% set test_cols = dbt_utils.get_column_values(table=ref('tests'), column='test_name') %}

WITH filtered AS (select
    state,
    {% for test in test_cols %}
    "{{ test }}" ,
    {% endfor %}
FROM {{ ref('test_results') }} 
)

-- Generate a table with two columns: state and list of tests run (not null)
SELECT
    state,
    {% for test in test_cols %}
    ARRAY_AGG("{{ test }}" ) AS "{{ test }}_list", 
    {% endfor %}
FROM filtered
GROUP BY STATE
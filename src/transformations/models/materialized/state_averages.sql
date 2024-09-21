{% set test_cols = dbt_utils.get_column_values(table=ref('tests'), column='test_name') %}


SELECT
    state,
    {% for test in test_cols %}
    -- Get the average for each test, checking for valid numeric values
    AVG(CASE WHEN 
        regexp_full_match(CAST("{{ test }}" AS VARCHAR), 
            '^[+-]?[0-9]*\.?[0-9]+$') 
            THEN CAST("{{ test }}" AS NUMERIC(38,10))
        ELSE 
            NULL 
        END) AS "{{ test }}_avg",
    {% endfor %}
FROM {{ ref('test_results') }}
GROUP BY STATE

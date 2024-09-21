{% set test_cols = dbt_utils.get_column_values(table=ref('tests'), column='test_name') %}

WITH filtered AS (select
    state,
    {% for test in test_cols %}
    "{{ test }}" ,
    {% endfor %}
from {{ ref('raw_test_results') }} 
)
select * from raw_test_results
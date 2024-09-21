{% macro count_non_nulls(table_name, columns) %}
    SELECT
        {% for column in columns %}
            SUM(CASE WHEN {{ column }} IS NOT NULL THEN 1 ELSE 0 END) AS {{ column }}_non_null_count{% if not loop.last %},{% endif %}
        {% endfor %}
    FROM {{ ref(table_name) }}
{% endmacro %}
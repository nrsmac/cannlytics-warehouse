{% macro get_test_names() %}
    {% set sql %}
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'raw_test_results'
        AND ordinal_position BETWEEN 8 AND 115;
    {% endset %}

    {% set results = run_query(sql) %}
    
    {% set columns = [] %}
    {% for row in results %}
        {% do columns.append(row[0].replace('_', '')) %}  -- Optionally clean names
    {% endfor %}
    {{ return(columns) }}
{% endmacro %}
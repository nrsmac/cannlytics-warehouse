{% macro combine_tables_from_schema(schema) %}
    {% set tables = dbt_utils.get_relations_by_prefix(schema=schema, prefix='') %}

    {% if tables | length == 0 %}
        select null as table_name
    {% else %}
        {% set union_query = [] %}
        
        {% set all_columns = [] %}

        -- First, gather all unique column names across all tables
        {% for table in tables %}
            {% set columns_query = "select column_name from information_schema.columns where table_schema = '" ~ schema ~ "' and table_name = '" ~ table.identifier ~ "'" %}
            {% set columns_results = run_query(columns_query) %}

            {% if columns_results is not none %}
                {% for column in columns_results %}
                    {% if column['column_name'] not in all_columns %}
                        {% do all_columns.append(column['column_name']) %}
                    {% endif %}
                {% endfor %}
            {% endif %}
        {% endfor %}
        
        -- Construct the union query
        {% for table in tables %}
            {% set coalesce_selects = [] %}
            {% set columns_query = "select column_name from information_schema.columns where table_schema = '" ~ schema ~ "' and table_name = '" ~ table.identifier ~ "'" %}
            {% set current_columns = run_query(columns_query) | map(attribute='column_name') | list %}

            {% for column in all_columns %}
                {% if column in current_columns %}
                    {% do coalesce_selects.append("\"" ~ column ~ "\"") %}
                {% else %}
                    {% do coalesce_selects.append("null as \"" ~ column ~ "\"") %}
                {% endif %}
            {% endfor %}
            
            {% do union_query.append("select " ~ coalesce_selects | join(', ') ~ " from \"" ~ schema ~ "\".\"" ~ table.identifier ~ "\"") %}
        {% endfor %}
        
        {{ return(union_query | join(' UNION ALL ')) }}
    {% endif %}
{% endmacro %}
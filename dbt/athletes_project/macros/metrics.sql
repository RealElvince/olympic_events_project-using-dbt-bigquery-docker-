-- macros/metrics.sql

-- Number of males
{% macro count_males(source_table) %}
    SELECT 
        COUNT(*) AS number_of_males
    FROM {{ ref(source_table) }}
    WHERE Sex = 'M'
{% endmacro %}

-- Number of females
{% macro count_females(source_table) %}
    SELECT 
        COUNT(*) AS number_of_females
    FROM {{ ref(source_table) }}
    WHERE Sex = 'F'
{% endmacro %}

-- Number of unique sports
{% macro count_unique_sports(source_table) %}
    SELECT 
        COUNT(DISTINCT Sport) AS total_sports
    FROM {{ ref(source_table) }}
{% endmacro %}

-- Number of unique events
{% macro count_unique_events(source_table) %}
    SELECT 
        COUNT(DISTINCT Event) AS total_events
    FROM {{ ref(source_table) }}
{% endmacro %}

-- Number of unique teams
{% macro count_unique_teams(source_table) %}
    SELECT 
        COUNT(DISTINCT Team) AS total_teams
    FROM {{ ref(source_table) }}
{% endmacro %}

-- Athletes with medals (Gold, Silver, Bronze)
{% macro athlete_with_medals(source_table, medal_gold, medal_silver, medal_bronze) %}
    SELECT
        athlete_id,
        Name AS athlete_name,
        COUNTIF(Medal = {{ medal_gold }}) AS gold_won,
        COUNTIF(Medal = {{ medal_silver }}) AS silver_won,
        COUNTIF(Medal = {{ medal_bronze }}) AS bronze_won
    FROM {{ source_table }}
    GROUP BY athlete_id, athlete_name
{% endmacro %}

-- Number of athletes with no medal
{% macro number_of_athletes_with_no_medal(source_table) %}
    SELECT
        COUNT(*) AS number_of_athletes_with_no_medals
    FROM {{ source_table }}
    WHERE Medal IS NULL 
{% endmacro %}

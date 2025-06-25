
 -- number of males
{{% macro count_males(source_table)% }}
 SELECT 
   COUNT(*) AS number_of_males
FROM {{ref(source_table)}}
WHERE Sex="M"
{{% endamcro%}}

-- number of females
{{% macro count_females(source_table)% }}
 SELECT 
   COUNT(*) AS number_of_sfemales
FROM {{ref(source_table)}}
WHERE Sex="F"
{{% endamcro%}}

-- number of sports
{% macro count_unique_sports(source_table) %}
    SELECT COUNT(DISTINCT Sport) AS total_sports
    FROM {{ ref(source_table) }}
{% endmacro %}

-- numbers of events
{% macro count_unique_events(source_table) %}
    SELECT COUNT(DISTINCT Event) AS total_events
    FROM {{ ref(source_table) }}
{% endmacro %}

-- numbers of teams
{% macro count_unique_teams(source_table) %}
    SELECT COUNT(distinct Team) AS total_teams
    FROM {{ ref(source_table) }}
{% endmacro %}
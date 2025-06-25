
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

--number of athletes with or no medal
-- macros/athlete_with_medals.sql

{% macro athlete_with_medals(source_table, medal_gold, medal_silver, medal_bronze) %}

SELECT
  athlete_id,
  Name AS athlete_name,
  COUNTIF(Medal = {{ medal_gold }}) AS gold_won,
  COUNTIF(Medal = {{ medal_silver }}) AS silver_won,
  COUNTIF(Medal = {{ medal_bronze }}) AS bronze_won
FROM {{ source_table }}
GROUP BY athlete_id,athlete_name

{% endmacro %}

--number of athletes with no medals
{{% macro number_of_athletes_with_no_medal(source_table)%}}
   SELECT
      COUNT(*) AS number_of_athletes_with_no_medals
   FROM {{source_table}}
   WHERE Medal IS NULL 
{{%endamcro%}}

-- models/marts/fct_team_medal_summary.sql
select
    Team,
    NOC,
    COUNT(*) AS total_entries,
    COUNTIF(Medal = 'Gold') AS gold_medals,
    COUNTIF(Medal = 'Silver') AS silver_medals,
    COUNTIF(Medal = 'Bronze') AS bronze_medals
FROM {{ ref('stg_athletes') }}
GROUP BY Team, NOC

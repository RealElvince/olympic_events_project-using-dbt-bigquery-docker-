SELECT DISTINCT
   athlete_id,
   Name AS athlete_name,
   Sex AS sex
FROM {{ref('stg_athletes')}}
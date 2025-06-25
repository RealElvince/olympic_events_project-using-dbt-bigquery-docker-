SELECT DISTINCT
  Sport AS sport,
  Event AS sport_event
FROM {{ref('stg_athletes')}}
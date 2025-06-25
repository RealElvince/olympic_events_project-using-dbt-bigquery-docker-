SELECT DISTINCT
  Team AS team,
  NOC AS noc

FROM {{ref('stg_athletes')}}
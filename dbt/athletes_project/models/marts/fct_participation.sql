
select
    athlete_id,
    Name AS athlete_name,
    COUNT(DISTINCT Games) as num_participations
FROM {{ ref('stg_athletes') }}
GROUP BY athlete_id, athlete_name
ORDER BY athlete_id,athlete_name
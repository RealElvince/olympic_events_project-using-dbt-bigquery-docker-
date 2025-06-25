
SELECT
    athlete_id,
    Name AS athlete_name,
    COUNT(DISTINCT  Year) AS appearances,
    STRING_AGG(DISTINCT CAST(Year AS string), ', ') AS years_participated
FROM {{ ref('stg_athletes') }}
GROUP BY athlete_id, athelete_name
HAVING appearances > 1


SELECT
    Sport,
    Event,
    AVG(Age) AS avg_age,
    MIN(Age) AS min_age,
    MAX(Age) AS max_age
FROM {{ ref('stg_athletes') }}
GROUP BY Sport, Event

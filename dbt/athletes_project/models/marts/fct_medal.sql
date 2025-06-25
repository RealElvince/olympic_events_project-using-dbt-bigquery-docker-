
SELECT
    athlete_id,
    Name,
    NOC,
    Team,
    Year,
    Season,
    Sport,
    Event,
    Medal
FROM{{ ref('stg_athletes') }}

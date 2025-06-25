

WITH source AS (

    SELECT 
       ID AS athlete_id,
       Name,
       Sex,
       Age,
       Height,
       Weight,
       Team,
       NOC,
       Games,
       Year,
       Season,
       City,
       Sport,
       Event,
       Medal
     FROM {{ source('olympic_dataset', 'athletes') }}

)

SELECT * FROM source

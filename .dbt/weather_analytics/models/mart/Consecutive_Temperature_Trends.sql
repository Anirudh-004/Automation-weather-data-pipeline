{{ config(materialized='table') }}

WITH ranked AS (
    SELECT *,
        ROW_NUMBER() OVER (ORDER BY weather_time_local) AS rn
    FROM {{ ref('staging') }}
)
SELECT
    rn,
    weather_time_local,
    temperature,
    LAG(temperature, 1) OVER (ORDER BY rn) AS prev_temp,
    temperature - LAG(temperature, 1) OVER (ORDER BY rn) AS temp_change
FROM ranked
ORDER BY rn

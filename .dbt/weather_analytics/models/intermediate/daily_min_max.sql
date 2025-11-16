{{ config(materialized='table') }}

SELECT
    date_trunc('day', weather_time_local) AS day,
    MAX(temperature) AS max_temperature,
    MIN(temperature) AS min_temperature,
    MAX(wind_speed) AS max_wind_speed,
    MIN(wind_speed) AS min_wind_speed
FROM {{ ref('staging') }}
GROUP BY 1
ORDER BY 1

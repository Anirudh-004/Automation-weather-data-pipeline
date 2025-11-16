{{ config(materialized='table') }}

SELECT
    weather_descriptions,
    AVG(temperature) AS avg_temp,
    AVG(wind_speed) AS avg_wind_speed
FROM {{ ref('staging') }}
GROUP BY weather_descriptions
ORDER BY avg_temp DESC

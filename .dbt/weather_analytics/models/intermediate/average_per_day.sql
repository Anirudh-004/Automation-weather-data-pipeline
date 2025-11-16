{{ config(materialized='table') }}

SELECT
    date_trunc('day', weather_time_local) AS day,
    AVG(temperature) AS avg_temperature,
    AVG(wind_speed) AS avg_wind_speed,
    COUNT(*) AS num_records
FROM {{ ref('staging') }}
GROUP BY 1
ORDER BY 1

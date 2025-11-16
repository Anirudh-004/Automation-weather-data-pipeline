{{ config(materialized='table') }}

SELECT
    date_trunc('week', weather_time_local) AS week_start,
    AVG(temperature) AS avg_temperature,
    AVG(wind_speed) AS avg_wind_speed,
    COUNT(*) AS num_records
FROM {{ ref('staging') }}
GROUP BY 1
ORDER BY 1

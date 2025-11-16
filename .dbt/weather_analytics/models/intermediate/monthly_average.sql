{{ config(materialized='table') }}

SELECT
    date_trunc('month', weather_time_local) AS month_start,
    AVG(temperature) AS avg_temperature,
    AVG(wind_speed) AS avg_wind_speed,
    COUNT(*) AS num_records
FROM {{ ref('staging') }}
GROUP BY 1
ORDER BY 1

{{ config(materialized='table') }}

SELECT
    date_trunc('week', weather_time_local) AS week_start,
    ROUND(AVG(temperature)::numeric, 2) AS avg_temperature,
    ROUND(AVG(wind_speed)::numeric, 2) AS avg_wind_speed,
    COUNT(*) AS num_records
FROM {{ ref('staging') }}
GROUP BY 1
ORDER BY 1

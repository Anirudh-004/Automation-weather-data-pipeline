{{ config(materialized='table') }}

SELECT
    day,
    avg_temperature,
    avg_wind_speed
FROM {{ ref('average_per_day') }}
ORDER BY day

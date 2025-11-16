{{ config(materialized='table') }}

SELECT
    weather_time_local,
    temperature,
    wind_speed,
    CASE 
        WHEN temperature >= 15  THEN 'sunny_day'
        WHEN temperature < 10 THEN 'cold_day'
        ELSE 'normal'
    END AS temp_flag,
    CASE
        WHEN wind_speed > 40 THEN 'high_wind'
        ELSE 'normal'
    END AS wind_flag
FROM {{ ref('staging') }}

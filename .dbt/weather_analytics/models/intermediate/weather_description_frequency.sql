{{ config(materialized='table') }}

SELECT
    weather_descriptions,
    COUNT(*) AS occurrences
FROM {{ ref('staging') }}
GROUP BY 1
ORDER BY occurrences DESC

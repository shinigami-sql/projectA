-- materialized='table' used for gold layer since there is no unique ID column to use for incremental, 
-- dbt drops and recreates the table on every run — standard approach for aggregate gold tables

{{config(materialized='table')}}

-- inserts count and percentage of figures plotted per dimension into gold table
-- ROUND divides count per dimension by total row count from subquery, multiplied by 100.0 to force decimal math
-- subquery runs independently of GROUP BY, returns total count across all rows

SELECT dimension_title as dimension, count(dimension_title) as count_of_figures_plotted, 
ROUND(count(dimension_title) * 100.0 / (SELECT count(*) FROM {{ref('plots_enriched')}}), 2) as percentage
FROM {{ref('plots_enriched')}}
GROUP BY 1
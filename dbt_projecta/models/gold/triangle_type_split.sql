-- materialized='table' used for gold layer since there is no unique ID column to use for incremental, 
-- dbt drops and recreates the table on every run — standard approach for aggregate gold tables

{{config(materialized='table')}}

-- inserts count and percentage of each triangle type into gold table
-- filters to Triangle figures only using WHERE figure_title = 'Triangle'
-- subquery counts total triangles only, used as denominator for percentage calculation
-- ROUND applies 2 decimal places, count multiplied by 100.0 to force decimal math
-- GROUP BY 1 groups by triangle_type_title

SELECT triangle_type_title as triangle_type, count(figure_title) as count_of_figures_plotted, 
ROUND(count(figure_title) * 100.0/(SELECT COUNT(figure_title) FROM {{ref('plots_enriched')}} WHERE figure_title = 'Triangle'), 2) as percentage
FROM {{ref('plots_enriched')}}
WHERE figure_title = 'Triangle'
GROUP BY 1
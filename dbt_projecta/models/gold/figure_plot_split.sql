-- materialized='table' used for gold layer since there is no unique ID column to use for incremental, 
-- dbt drops and recreates the table on every run — standard approach for aggregate gold tables

{{config(materialized='table')}}

-- inserts count and percentage of each figure type into gold table
-- subquery counts total rows in silver as denominator for percentage calculation
-- ROUND applies 2 decimal places, count multiplied by 100.0 to force decimal math
-- GROUP BY 1 groups by figure_title

SELECT figure_title as figure, COUNT(figure_title) as count_of_figures_plotted, 
ROUND(COUNT(figure_title) * 100.0 / (SELECT COUNT(figure_title) FROM {{ref('plots_enriched')}}), 2) as percentage
FROM {{ref('plots_enriched')}}
GROUP BY 1
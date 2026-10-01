-- materialized='table' used for gold layer since there is no unique ID column to use for incremental, 
-- dbt drops and recreates the table on every run — standard approach for aggregate gold tables

{{config(materialized='table')}}

-- inserts total count of all figures plotted across all sessions into gold table
-- COUNT(figure_title) counts all rows in silver.plots_enriched
 
SELECT COUNT(figure_title) as count_of_figures_plotted
FROM {{ref('plots_enriched')}}
{{config(materialized='table')}}

SELECT is_weekday as weekday, COUNT(figure_title) count_of_figures_plotted, round(count(figure_title) * 100.0 / (select count(*) from silver.plots_enriched), 2) as percentage
FROM {{ref('plots_enriched')}}
group by 1

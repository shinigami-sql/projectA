{{config(materialized='table')}}

-- RANK() is a window function that assigns a rank to each row within a partition
-- OVER connects RANK() to the window definition
-- PARTITION BY defines the groups to rank within, ORDER BY defines what to rank by
-- rank 1 is the most plotted figure within each partition

SELECT figure_title as figure, is_weekday, COUNT(figure_title) as count_of_figures_plotted, 
RANK() OVER (PARTITION BY is_weekday ORDER BY COUNT(figure_title) DESC)
FROM {{ref('plots_enriched')}}
GROUP BY 1, 2
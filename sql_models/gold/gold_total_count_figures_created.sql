INSERT INTO gold.total_count_figures_created (total_figures) 
SELECT COUNT(figure_title) 
FROM silver.plots_enriched;
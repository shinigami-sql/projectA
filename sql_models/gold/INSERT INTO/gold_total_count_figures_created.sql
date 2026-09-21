-- inserts total count of all figures plotted across all sessions into gold table
-- COUNT(figure_title) counts all rows in silver.plots_enriched

INSERT INTO gold.total_count_figures_created (total_figures) 
SELECT COUNT(figure_title) 
FROM silver.plots_enriched;
-- inserts count and percentage of each figure type into gold table
-- subquery counts total rows in silver as denominator for percentage calculation
-- ROUND applies 2 decimal places, count multiplied by 100.0 to force decimal math
-- GROUP BY 1 groups by figure_title

INSERT INTO gold.figure_plot_split (figure_title, plot_count, plot_percentage)
SELECT figure_title, COUNT(figure_title), 
ROUND(COUNT(figure_title) * 100.0 / (SELECT COUNT(figure_title) FROM silver.plots_enriched), 2)
FROM silver.plots_enriched
GROUP BY 1;
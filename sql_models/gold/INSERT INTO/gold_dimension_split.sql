-- inserts count and percentage of figures plotted per dimension into gold table
-- ROUND divides count per dimension by total row count from subquery, multiplied by 100.0 to force decimal math
-- subquery runs independently of GROUP BY, returns total count across all rows

INSERT INTO gold.dimension_split (dimension, plot_count, plot_percentage)
SELECT dimension_title, count(dimension_title), 
ROUND(count(dimension_title) * 100.0 / (SELECT count(*) From silver.plots_enriched), 2)
FROM silver.plots_enriched
GROUP BY 1;
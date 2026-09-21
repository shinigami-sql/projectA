-- inserts count and percentage of each triangle type into gold table
-- filters to Triangle figures only using WHERE figure_title = 'Triangle'
-- subquery counts total triangles only, used as denominator for percentage calculation
-- ROUND applies 2 decimal places, count multiplied by 100.0 to force decimal math
-- GROUP BY 1 groups by triangle_type_title

INSERT INTO gold.triangle_type_split (Triangle_type, plot_count, plot_percentage)
SELECT triangle_type_title, count(figure_title), 
ROUND(count(figure_title) * 100.0/(SELECT COUNT(figure_title) FROM silver.plots_enriched WHERE figure_title = 'Triangle'), 2)
FROM silver.plots_enriched
WHERE figure_title = 'Triangle'
GROUP BY 1;
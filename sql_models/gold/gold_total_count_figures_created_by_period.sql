-- inserts count of figures plotted per day of week into gold table
-- 'Day of Week' hardcoded as period_type, day_of_week column as period_value, count(figure_title) as period_count
-- ordered Sunday to Saturday using CASE TRIM since 
-- TO_CHAR fills day names to 9 characters with trailing spaces, 
-- TRIM strips those trailing spaces before comparing so the CASE WHEN matches correctly

INSERT INTO gold.total_count_figures_created_by_period (period_type, period_value, period_count)
SELECT 'Day of Week', day_of_week, count(figure_title)
FROM silver.plots_enriched
GROUP BY 2
ORDER BY CASE TRIM(day_of_week)
WHEN 'Sunday' THEN 1
WHEN 'Monday' THEN 2
WHEN 'Tuesday' THEN 3
WHEN 'Wednesday' THEN 4
WHEN 'Thursday' THEN 5
WHEN 'Friday' THEN 6
WHEN 'Saturday' THEN 7
END;


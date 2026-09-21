-- DAY OF WEEK
-- inserts count of figures plotted per day of week into gold table
-- 'Day of Week' hardcoded as period_type, day_of_week column as period_value, count(figure_title) as period_count
-- ordered Sunday to Saturday using CASE TRIM since 
-- TO_CHAR fills day names to 9 characters with trailing spaces, 
-- TRIM strips those trailing spaces before comparing so the CASE WHEN matches correctly

INSERT INTO gold.total_count_figures_created_by_period (period_type, period_value, year, period_count)
SELECT 'Day of Week', day_of_week, year::INTEGER, count(figure_title)
FROM silver.plots_enriched
GROUP BY 2, 3
ORDER BY CASE TRIM(day_of_week)
WHEN 'Sunday' THEN 1
WHEN 'Monday' THEN 2
WHEN 'Tuesday' THEN 3
WHEN 'Wednesday' THEN 4
WHEN 'Thursday' THEN 5
WHEN 'Friday' THEN 6
WHEN 'Saturday' THEN 7
END;

-- WEEK OF MONTH
-- inserts count of figures plotted per week of month into gold table
-- 'Week of Month' hardcoded as period_type, week_of_month column as period_value, count(figure_title) as period_count
-- ordered 1 to 5 using ORDER BY 2 since week_of_month is now INTEGER in silver, numeric ordering is correct by default
-- year added to GROUP BY since it is a non-aggregated column in SELECT

INSERT INTO gold.total_count_figures_created_by_period (period_type, period_value, year, period_count) 
SELECT 'Week of Month', week_of_month, year::INTEGER, count(figure_title)
FROM silver.plots_enriched
GROUP BY 2, 3
ORDER BY 2;

-- WEEK OF YEAR
-- inserts count of figures plotted per week of year into gold table
-- 'Week of Year' hardcoded as period_type, week_of_year column as period_value, count(figure_title) as period_count
-- ordered 1 to 53 using ORDER BY 2 since week_of_year is now INTEGER in silver, numeric ordering is correct by default
-- year added to GROUP BY since it is a non-aggregated column in SELECT

INSERT INTO gold.total_count_figures_created_by_period (period_type, period_value, year, period_count) 
SELECT 'Week of Year', week_of_year, year::INTEGER, count(figure_title)
FROM silver.plots_enriched
GROUP BY 2, 3
ORDER BY 2;

-- MONTH
-- inserts count of figures plotted per month into gold table
-- 'Month' hardcoded as period_type, month column as period_value, count(figure_title) as period_count
-- ordered January to December using CASE TRIM since TO_CHAR fills month names with trailing spaces,
-- TRIM strips those trailing spaces before comparing so the CASE WHEN matches correctly and rows are inserted in chronological order into the gold table
-- year added to GROUP BY since it is a non-aggregated column in SELECT

INSERT INTO gold.total_count_figures_created_by_period (period_type, period_value, year, period_count) 
SELECT 'Month', month, year::INTEGER, count(figure_title)
FROM silver.plots_enriched
GROUP BY 2, 3
ORDER BY CASE TRIM(month) 
WHEN 'January' then 1
WHEN 'February' then 2
WHEN 'March' then 3
WHEN 'April' then 4
WHEN 'May' then 5
WHEN 'June' then 6
WHEN 'July' then 7
WHEN 'August' then 8
WHEN 'September' then 9
WHEN 'October' then 10
WHEN 'November' then 11
WHEN 'December' then 12
END;

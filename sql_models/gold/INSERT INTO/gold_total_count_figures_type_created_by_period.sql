-- DAY OF WEEK
-- inserts count of figures plotted per figure type per day of week into gold table
-- year cast to INTEGER, ordered Sunday to Saturday using CASE TRIM since TO_CHAR fills day names with trailing spaces
-- GROUP BY 1, 3, 4 groups by figure_title, day_of_week and year

INSERT INTO gold.total_count_figures_type_created_by_period (figure_title, period_type, period_value, year, period_count)
SELECT figure_title, 'Day of Week' as day_of_week, day_of_week, year::INTEGER, count(figure_title)
FROM silver.plots_enriched
GROUP BY 1, 3, 4
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
-- inserts count of figures plotted per figure type per week of month into gold table
-- year cast to INTEGER, ordered by week number ascending since week_of_month is INTEGER in silver
-- GROUP BY 1, 3, 4 groups by figure_title, week_of_month and year

INSERT INTO gold.total_count_figures_type_created_by_period (figure_title, period_type, period_value, year, period_count)
SELECT figure_title, 'Week of Month' as week_of_month, week_of_month, year::INTEGER, count(figure_title)
FROM silver.plots_enriched
GROUP BY 1, 3, 4
ORDER BY 3;

-- WEEK OF YEAR
-- inserts count of figures plotted per figure type per week of year into gold table
-- year cast to INTEGER, ordered by week number ascending since week_of_year is INTEGER in silver
-- GROUP BY 1, 3, 4 groups by figure_title, week_of_year and year

INSERT INTO gold.total_count_figures_type_created_by_period (figure_title, period_type, period_value, year, period_count)
SELECT figure_title, 'Week of Year' as week_of_year, week_of_year, year::INTEGER, count(figure_title)
FROM silver.plots_enriched
GROUP BY 1, 3, 4
ORDER BY 3;

-- MONTH
-- inserts count of figures plotted per figure type per month into gold table
-- year cast to INTEGER, ordered January to December using CASE TRIM since TO_CHAR fills month names with trailing spaces
-- GROUP BY 1, 3, 4 groups by figure_title, month and year

INSERT INTO gold.total_count_figures_type_created_by_period (figure_title, period_type, period_value, year, period_count)
SELECT figure_title, 'Month' as month, month, year::INTEGER, count(figure_title)
FROM silver.plots_enriched
GROUP BY 1, 3, 4
ORDER BY CASE TRIM(month)
WHEN 'January' THEN 1
WHEN 'February' THEN 2
WHEN 'March' THEN 3
WHEN 'April' THEN 4
WHEN 'May' THEN 5
WHEN 'June' THEN 6
WHEN 'July' THEN 7
WHEN 'August' THEN 8
WHEN 'September' THEN 9
WHEN 'October' THEN 10
WHEN 'November' THEN 11
WHEN 'December' THEN 12
END;

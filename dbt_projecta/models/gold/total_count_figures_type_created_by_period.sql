-- materialized='table' used for gold layer since there is no unique ID column to use for incremental
-- dbt drops and recreates the table on every run — standard approach for aggregate gold tables

{{config(materialized='table')}}

-- neither UNION nor UNION ALL allow ORDER BY inside individual SELECT statements
-- each SELECT is wrapped in a subquery so ORDER BY can be applied per period type before combining results
-- UNION ALL used instead of UNION since UNION removes duplicate rows which is not desired here

-- DAY OF WEEK
-- inserts count of figures plotted per figure type per day of week into gold table
-- year cast to INTEGER, ordered Sunday to Saturday using CASE TRIM since TO_CHAR fills day names with trailing spaces
-- GROUP BY 1, 3, 4 groups by figure_title, day_of_week and year

-- WEEK OF MONTH
-- inserts count of figures plotted per figure type per week of month into gold table
-- year cast to INTEGER, ordered by week number ascending since week_of_month is INTEGER in silver
-- GROUP BY 1, 3, 4 groups by figure_title, week_of_month and year

-- WEEK OF YEAR
-- inserts count of figures plotted per figure type per week of year into gold table
-- year cast to INTEGER, ordered by week number ascending since week_of_year is INTEGER in silver
-- GROUP BY 1, 3, 4 groups by figure_title, week_of_year and year

-- MONTH
-- inserts count of figures plotted per figure type per month into gold table
-- year cast to INTEGER, ordered January to December using CASE TRIM since TO_CHAR fills month names with trailing spaces
-- GROUP BY 1, 3, 4 groups by figure_title, month and year

-- UNION ALL requires the same number of columns in the same order across all SELECT statements
-- the data type of each column must also match across all SELECTs — if position 2 is TEXT in one SELECT it must be TEXT in all
-- week_of_month and week_of_year are INTEGER in silver but cast to TEXT here so they match the TEXT type of other period values in the UNION
-- failing to match types throws: UNION types text and integer cannot be matched


SELECT * FROM (SELECT figure_title as figure, 'Day of Week' as period_type, day_of_week as period_value, year::INTEGER as year, count(figure_title) as period_count
FROM {{ref('plots_enriched')}}
GROUP BY 1, 3, 4
ORDER BY CASE TRIM(day_of_week)
WHEN 'Sunday' THEN 1
WHEN 'Monday' THEN 2
WHEN 'Tuesday' THEN 3
WHEN 'Wednesday' THEN 4
WHEN 'Thursday' THEN 5
WHEN 'Friday' THEN 6
WHEN 'Saturday' THEN 7
END) as day_of_week

UNION ALL

SELECT * FROM (SELECT figure_title as figure, 'Week of Month' as period_type, week_of_month::TEXT as period_value, year::INTEGER as year, count(figure_title) as period_count
FROM {{ref('plots_enriched')}}
GROUP BY 1, 3, 4
ORDER BY 3) as week_of_month

UNION ALL


SELECT * FROM (SELECT figure_title as figure, 'Week of Year' as period_type, week_of_year::TEXT as period_value, year::INTEGER as year, count(figure_title) as period_count
FROM {{ref('plots_enriched')}}
GROUP BY 1, 3, 4
ORDER BY 3) as week_of_year

UNION ALL

SELECT * FROM (SELECT figure_title as figure, 'Month' as period_type, month as period_value, year::INTEGER as year, count(figure_title) as period_count
FROM {{ref('plots_enriched')}}
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
END) as month

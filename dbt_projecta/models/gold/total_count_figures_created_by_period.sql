-- materialized='table' used for gold layer since there is no unique ID column to use for incremental, 
-- dbt drops and recreates the table on every run — standard approach for aggregate gold tables

{{config(materialized='table')}} 

-- each SELECT is wrapped in a subquery since neither UNION nor UNION ALL allow ORDER BY inside individual SELECT statements
-- wrapping in a subquery applies ORDER BY first, then UNION ALL combines the already-ordered results
-- UNION ALL used instead of UNION since UNION removes duplicate rows which is not desired here


-- DAY OF WEEK
-- inserts count of figures plotted per day of week into gold table
-- 'Day of Week' hardcoded as period_type, day_of_week column as period_value, count(figure_title) as period_count
-- ordered Sunday to Saturday using CASE TRIM since 
-- TO_CHAR fills day names to 9 characters with trailing spaces, 
-- TRIM strips those trailing spaces before comparing so the CASE WHEN matches correctly

-- WEEK OF MONTH
-- inserts count of figures plotted per week of month into gold table
-- 'Week of Month' hardcoded as period_type, week_of_month column as period_value, count(figure_title) as period_count
-- ordered 1 to 5 using ORDER BY 2 since week_of_month is now INTEGER in silver, numeric ordering is correct by default
-- year added to GROUP BY since it is a non-aggregated column in SELECT

-- WEEK OF YEAR
-- inserts count of figures plotted per week of year into gold table
-- 'Week of Year' hardcoded as period_type, week_of_year column as period_value, count(figure_title) as period_count
-- ordered 1 to 53 using ORDER BY 2 since week_of_year is now INTEGER in silver, numeric ordering is correct by default
-- year added to GROUP BY since it is a non-aggregated column in SELECT


-- MONTH
-- inserts count of figures plotted per month into gold table
-- 'Month' hardcoded as period_type, month column as period_value, count(figure_title) as period_count
-- ordered January to December using CASE TRIM since TO_CHAR fills month names with trailing spaces,
-- TRIM strips those trailing spaces before comparing so the CASE WHEN matches correctly and rows are inserted in chronological order into the gold table
-- year added to GROUP BY since it is a non-aggregated column in SELECT

-- UNION ALL requires the same number of columns in the same order across all SELECT statements
-- the data type of each column must also match across all SELECTs — if position 2 is TEXT in one SELECT it must be TEXT in all
-- week_of_month and week_of_year are INTEGER in silver but cast to TEXT here so they match the TEXT type of other period values in the UNION
-- failing to match types throws: UNION types text and integer cannot be matched


SELECT * FROM (SELECT 'Day of Week' as period_type, day_of_week as period_value, year::INTEGER as year, count(figure_title) as period_count
FROM {{ref('plots_enriched')}}
GROUP BY 2, 3
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

SELECT * FROM (SELECT 'Week of Month' as period_type, week_of_month::TEXT as period_value, year::INTEGER as year, count(figure_title) as period_count
FROM {{ref('plots_enriched')}}
GROUP BY 2, 3
ORDER BY 2) as week_of_month

UNION ALL

SELECT * FROM (SELECT 'Week of Year' as period_type, week_of_year::TEXT as period_value, year::INTEGER as year, count(figure_title) as period_count
FROM {{ref('plots_enriched')}}
GROUP BY 2, 3
ORDER BY 2) as week_of_year

UNION ALL

SELECT * FROM (SELECT 'Month' as period_type, month as period_value, year::INTEGER as year, count(figure_title) as period_count
FROM {{ref('plots_enriched')}}
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
END) as month


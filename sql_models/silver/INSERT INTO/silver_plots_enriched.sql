-- inserts new rows from raw.plots into silver.plots_enriched, skipping rows already in silver using WHERE id NOT IN
-- transforms raw data: INITCAP standardizes figure and dimension text to title case
-- CASE WHEN maps triangle_type codes e, i, r to full names Equilateral, Isosceles, Right Triangle
-- CASE WHEN maps dimension 2d/3d to uppercase 2D/3D
-- CAST splits timestamp into DATE and TIME components
-- TO_CHAR(date, 'Day') extracts full day name, pads to 9 characters with trailing spaces
-- TO_CHAR(date, 'D') returns day of week as a number, 1 for Sunday and 7 for Saturday, used to flag is_weekday
-- TO_CHAR(date, 'W')::INTEGER returns week number within the month (1-5) cast to INTEGER for correct numeric ordering
-- TO_CHAR(date, 'WW')::INTEGER returns week number within the year (1-53) cast to INTEGER for correct numeric ordering
-- TO_CHAR(date, 'Month') returns full month name
-- TO_CHAR(date, 'YYYY') returns 4-digit year

INSERT INTO silver.plots_enriched (plot_turn, figure_title, is_triangle, triangle_type_title, dimension_title, rotation, date, time, day_of_week, is_weekday, week_of_month, week_of_year, month, year)
SELECT plot_turn as plot_turn,
INITCAP(figure) as figure_title,
CASE WHEN INITCAP(figure) = 'Triangle' THEN TRUE else FALSE END AS is_triangle,
CASE WHEN triangle_type = 'e' THEN 'Equilateral'
WHEN triangle_type = 'i' THEN 'Isoceles'
WHEN triangle_type = 'r' THEN 'Right Triangle' END AS triangle_type_title,
CASE WHEN dimension = '2d' THEN '2D'
WHEN dimension = '3d' THEN '3D' END AS dimension_title,
rotation as rotation,
CAST(date as DATE) as date,
date::TIME as time,
TO_CHAR(date, 'Day') as day_of_week,
CASE WHEN TO_CHAR(date, 'D') IN ('1', '7') THEN FALSE ELSE TRUE END AS is_weekday,
TO_CHAR(date, 'W')::INTEGER as week_of_month,
TO_CHAR(date, 'WW')::INTEGER as week_of_year,
TO_CHAR(date, 'Month') as month,
TO_CHAR(date, 'YYYY') as year
FROM raw.plots
WHERE id NOT IN (SELECT id FROM silver.plots_enriched);
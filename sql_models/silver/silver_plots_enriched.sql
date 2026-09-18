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
TO_CHAR(date, 'W') as week_of_month,
TO_CHAR(date, 'WW') as week_of_year,
TO_CHAR(date, 'Month') as month,
TO_CHAR(date, 'YYYY') as year
FROM raw.plots
WHERE id NOT IN (SELECT id FROM silver.plots_enriched);
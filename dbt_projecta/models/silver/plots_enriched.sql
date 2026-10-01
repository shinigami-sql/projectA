
-- materialized='incremental', dbt uses this column to identify what already exists vs what is new
-- unique_key='id', tells dbt to only insert new rows on each run, not drop and recreate

{{ config(materialized='incremental', unique_key='id') }}

-- plots_enriched.sql - silver layer model
-- transforms raw.plots into silver.plots_enriched
-- on first run dbt creates the table with all data
-- on subsequent runs only new rows are inserted using the is_incremental() block
-- transforms raw data: INITCAP standardizes figure and dimension text to title case
-- CASE WHEN maps triangle_type codes e, i, r to full names Equilateral, Isosceles, Right Triangle
-- CASE WHEN maps dimension 2d/3d to uppercase 2D/3D
-- CAST splits timestamp into DATE and TIME components

-- TO_CHAR(date, 'Day') extracts the full day name but pads it to 9 characters with trailing spaces
-- TRIM applied to remove trailing spaces so accepted_values dbt test matches correctly
-- Also applied it on 'TO_CHAR(date, 'Month')

-- TO_CHAR(date, 'D') returns day of week as a number, 1 for Sunday and 7 for Saturday, used to flag is_weekday
-- TO_CHAR(date, 'W')::INTEGER returns week number within the month (1-5) cast to INTEGER for correct numeric ordering
-- TO_CHAR(date, 'WW')::INTEGER returns week number within the year (1-53) cast to INTEGER for correct numeric ordering
-- TO_CHAR(date, 'Month') returns full month name
-- TO_CHAR(date, 'YYYY') returns 4-digit year

SELECT id, plot_turn,
INITCAP(figure) AS figure_title,
CASE WHEN INITCAP(figure) = 'Triangle' THEN TRUE ELSE FALSE END AS is_triangle,
CASE WHEN triangle_type = 'e' THEN 'Equilateral'
WHEN triangle_type = 'i' THEN 'Isoceles'
WHEN triangle_type = 'r' THEN 'Right Triangle' END AS triangle_type_title,
CASE WHEN dimension = '2d' THEN '2D'
WHEN dimension = '3d' THEN '3D' END AS dimension_title,
rotation,
CAST(date AS DATE) AS date,
date::TIME AS time,
TRIM(TO_CHAR(date, 'Day')) AS day_of_week,
CASE WHEN TO_CHAR(date, 'D') IN ('1', '7') THEN FALSE ELSE TRUE END AS is_weekday,
TO_CHAR(date, 'W')::INTEGER AS week_of_month,
TO_CHAR(date, 'WW')::INTEGER AS week_of_year,
TRIM(TO_CHAR(date, 'Month')) AS month,
TO_CHAR(date, 'YYYY')::INTEGER AS year
FROM {{ source('raw', 'plots') }} -- source() references tables dbt did not create, 'raw' is the source name from schema.yml, 'plots' is the table

{% if is_incremental() %} -- runs only when materialized='incremental' and the table already exists in the database. On the first run dbt creates the table with all data, subsequent runs only insert new rows
WHERE id NOT IN (SELECT id FROM {{ this }}) -- {{ this }} refers to this model's own table in the database, filters out rows that already exist
{% endif %} -- closes the if block
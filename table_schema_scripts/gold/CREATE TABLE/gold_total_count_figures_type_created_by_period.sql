-- creates gold table to store count of plots per figure type per time period
-- figure_title groups by figure, period_type and period_value define the time dimension, year added as dimension column, period_count is the aggregate

CREATE TABLE gold.total_count_figures_type_created_by_period (
figure_title TEXT,
period_type TEXT,
period_value TEXT,
year INTEGER,
period_count INTEGER
);
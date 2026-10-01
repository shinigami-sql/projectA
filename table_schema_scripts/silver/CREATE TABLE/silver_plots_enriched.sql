CREATE TABLE silver.plots_enriched (
    id SERIAL PRIMARY KEY,
    plot_turn INTEGER,
    figure_title TEXT,
    is_triangle BOOLEAN,
    triangle_type_title TEXT,
    dimension_title TEXT,
    rotation BOOLEAN,
    date DATE,
    time TIME,
    day_of_week TEXT,
    is_weekday BOOLEAN,
    week_of_month INTEGER,
    week_of_year INTEGER,
    month TEXT,
    year TEXT
);
-- creates gold table to store count and percentage of plots per figure type

CREATE TABLE gold.figure_plot_split(
    figure_title TEXT,
    plot_count INTEGER,
    plot_percentage DECIMAL
);
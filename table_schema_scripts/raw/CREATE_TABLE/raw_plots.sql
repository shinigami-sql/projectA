CREATE TABLE raw.plots (
    id SERIAL PRIMARY KEY,
    plot_turn INTEGER,
    figure TEXT,
    triangle_type TEXT,
    dimension TEXT,
    rotation BOOLEAN,
    date TIMESTAMP
);
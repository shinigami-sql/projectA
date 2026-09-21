-- creates gold table to store count and percentage of plots per dimension (2D vs 3D)

CREATE TABLE gold.dimension_split(
dimension TEXT,
plot_count INTEGER,
plot_percentage DECIMAL);
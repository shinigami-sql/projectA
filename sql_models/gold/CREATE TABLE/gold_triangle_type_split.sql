-- creates gold table to store count and percentage of plots per triangle type (Isosceles, Equilateral, Right Triangle)

CREATE TABLE gold.triangle_type_split(
Triangle_type TEXT, 
plot_count INTEGER, 
plot_percentage DECIMAL);
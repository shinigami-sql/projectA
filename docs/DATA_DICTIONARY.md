# Data Dictionary — raw.plots

The raw table where every plot lands untouched, from both the interactive UI (`main.py`) and the automated data generator (`data_pipeline/data_generator.py`). One row = one plotted figure. Cleaning and standardizing happens later in the silver layer (`plots_enriched`).

| Column | Type | Description | Possible values |
|--------|------|-------------|-----------------|
| `id` | integer | Unique ID of each plot row. | Increasing whole numbers |
| `plot_turn` | integer | Position of the plot within its session — first plot of a session, second, and so on. Starts at 1. | Whole numbers from 1 |
| `figure` | text | The geometric figure plotted. | Figures from `list_of_figures` in `constants.py`, e.g. `triangle` |
| `triangle_type` | text | Type of triangle, stored as a one-letter code. Only filled when `figure` is a triangle. | `i` (isosceles), `r` (right), `e` (equilateral), or `NULL` for any other figure |
| `dimension` | text | Whether the figure was plotted in 2D or 3D. | `2d`, `3d` |
| `rotation` | boolean | Whether the plot was rotated. Only 3D plots rotate, automatically. | `true` for 3D plots, `false` for 2D plots |
| `date` | timestamp without time zone | Date and time the plot was generated. For the interactive UI, this is when the plot was made, not when the session's plots were inserted into the database. | Any timestamp |

## Notes

- Text values aren't standardized in raw: casing can differ between the UI and the generator. `plots_enriched` standardizes them.
- `triangle_type` codes are mapped to full names in `plots_enriched`.
- `triangle_type` is `False` in the local JSON session log for non-triangles, but lands as `NULL` in this table.
- `date` has no time zone attached.
- Rows inserted by the data generator before the `plot_turn` fix start at 0 instead of 1. From the fix onward, both the UI and the generator start at 1.
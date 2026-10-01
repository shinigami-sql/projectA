# projectA
This is an educational project to practice Python and its libraries, exploring data engineering concepts by building a real pipeline from scratch.

The program offers two ways to generate data. The interactive UI prompts the user to select a geometric figure and choose between 2D or 3D, plots it and applies rotation automatically for 3D. Each plot is logged locally as JSON throughout the session, and when the session ends all plots are inserted into the raw plots table on Supabase. The other way is the data generator, which populates the database with 1 to 25 random plot entries per run via GitHub Actions running 4 times daily. A dbt transformation layer runs on a separate GitHub Actions schedule, transforming raw data through silver and gold layers with automated data quality tests.
## How to run

Create a `.env` file in the project root with a `DATABASE_URL` variable pointing to your database — this makes the project plug and play, swap the value for local or production without changing any code.

**Interactive UI** — select a figure, plot it and each plot is logged as JSON and inserted into the database:

```bash
python3 main.py  # macOS/Linux
python main.py   # Windows
```

**Data generator** — generates 1 to 25 random plot entries and inserts them directly into the database:

```bash
python3 data_pipeline/data_generator.py  # macOS/Linux
python data_pipeline/data_generator.py   # Windows
```

## Libraries
- matplotlib
- numpy
- pandas
- psycopg2
- python-dotenv
- logging (built-in)
- os (built-in)
- sys (built-in)
- datetime (built-in)
- json (built-in)
- random (built-in)

## Tools
- dbt-postgres
- PostgreSQL
- Supabase

## What's new?
- Added dbt transformation layer with silver and gold data models
- Silver model `plots_enriched` transforms and enriches raw plot data
- Gold models answer business questions on figure counts, dimension splits, triangle types, weekday vs weekend splits, time-based breakdowns and figure rankings per period using RANK() window function
- Added data quality tests using `not_null`, `unique`, `accepted_values` and `dbt_utils.expression_is_true` across silver layer columns
- Added `generate_schema_name` macro to override dbt default schema naming behavior
- Added GitHub Actions workflow running 1 hour after each data generator to execute `dbt run` and `dbt test` automatically
- Dagster not used, project complexity does not require a full orchestrator, GitHub Actions handles scheduling

## What's next?
projectA is complete. The full pipeline is operational, raw data lands daily via GitHub Actions, dbt transforms it through silver and gold layers via a separate GitHub Actions workflow, data quality is enforced via automated tests.
# projectA

This is an educational project to practice Python and its libraries, exploring data engineering concepts by building a real pipeline from scratch.

The program prompts the user to select a geometric figure and choose between 2D or 3D. Selecting 3D applies rotation automatically. Data is logged locally as JSON and inserted into a PostgreSQL database on Supabase, populated daily via a GitHub Actions workflow.

## How to run

Create a `.env` file in the project root with a `DATABASE_URL` variable pointing to your database — this makes the project plug and play, swap the value for local or production without changing any code.

**Interactive UI** — select a figure, plot it and each plot is automatically inserted into the database:

```bash
python3 main.py  # macOS/Linux
python main.py   # Windows
```

**Data generator** — generates 1 to 25 random plot entries and inserts them into the database:

```bash
python3 data/data_generator.py  # macOS/Linux
python data/data_generator.py   # Windows
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

## What's new?
- Added Supabase as the cloud PostgreSQL database
- Set up raw, silver and gold schemas in Supabase to support a structured data pipeline
- Added `.env` file with `python-dotenv` to load environment variables locally, keeping credentials out of the code
- Built `data_generator.py` to populate the database with random plot data
- Added GitHub Actions workflow running 4 times daily that executes `data_generator.py` automatically, with full documentation in `GITHUB_ACTIONS.md`

## What's next?
Build data models on top of the plots table using dbt, orchestrated by Dagster.
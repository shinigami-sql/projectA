# projectA

This is an educational project to practice Python and its libraries, exploring data engineering concepts by building a real pipeline from scratch.

The program prompts the user to select a geometric figure, choose between 2D or 3D, plots it and applies rotation (3D only). Figure coordinates are generated dynamically using numpy in `plot_engine.py`, no CSV needed. `main.py` handles user input and control flow, `constants.py` stores all static message strings, `logfile_generator.py` configures activity logging, and `session_logger.py` generates a JSON file per session and inserts plot data into a PostgreSQL database hosted on Supabase. A GitHub Actions workflow runs automatically 4 times daily, generating random plot data and inserting it into Supabase to support future data models and reporting.

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
- Created raw, silver and gold schemas in Supabase to support a structured data pipeline
- Created `.env` file with `python-dotenv` to load environment variables locally, keeping credentials out of the code
- Created `data_generator.py` to populate the database with random plot data
- Added GitHub Actions workflow running 4 times daily that executes `data_generator.py` automatically

## What's next?
Build data models on top of the plots table using dbt, orchestrated by Dagster.
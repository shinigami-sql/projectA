# dbt_projecta

dbt (data build tool) transformation layer for projectA. Runs SQL transformations against the Supabase PostgreSQL database, generating silver and gold layer tables from raw data loaded by GitHub Actions.

## Project structure

```
dbt_projecta/
├── dbt_project.yml       # project config: name, profile, folder-to-schema mappings
├── packages.yml          # dbt package dependencies (dbt_utils)
├── models/
│   ├── schema.yml        # source definitions and data quality tests
│   ├── silver/
│   │   └── plots_enriched.sql
│   └── gold/
│       ├── dimension_split.sql
│       ├── figure_plot_split.sql
│       ├── total_count_figures_created.sql
│       ├── total_count_figures_created_by_period.sql
│       ├── total_count_figures_type_created_by_period.sql
│       └── triangle_type_split.sql
└── macros/
    └── generate_schema_name.sql
```

## Configuration

`dbt_project.yml` holds the project name, the database profile to use, folder paths and the mapping between model folders and Supabase schemas:

- `models/silver/` → `silver` schema in Supabase
- `models/gold/` → `gold` schema in Supabase

`profiles.yml` lives at `~/.dbt/profiles.yml` and holds the Supabase database credentials.

## Macros

### generate_schema_name
Overrides dbt's built-in `generate_schema_name` macro. By default dbt concatenates the target schema (`public`) with custom schemas giving `public_silver` and `public_gold`. This macro returns the custom schema name directly — `silver` or `gold` — without any prefix.

## Models

### Silver layer

| Model | Description |
|-------|-------------|
| `plots_enriched` | Transforms `raw.plots` into a clean enriched table. Standardizes figure and dimension text, maps triangle type codes to full names, splits timestamp into date and time components, derives day of week, week of month, week of year, month and year. Incremental materialization — only inserts new rows. |

### Gold layer

| Model | Question it answers |
|-------|---------------------|
| `total_count_figures_created` | How many figures have been plotted in total? |
| `total_count_figures_created_by_period` | How many figures were plotted per day of week, week of month, week of year and month? |
| `total_count_figures_type_created_by_period` | How many of each figure type were plotted per time period? |
| `dimension_split` | What is the count and percentage split between 2D and 3D plots? |
| `figure_plot_split` | What is the count and percentage of each figure type plotted? |
| `triangle_type_split` | What is the count and percentage of each triangle type plotted? |

## Data quality tests

Data quality tests are defined in schema.yml and run with dbt test. Tests include not_null, unique, accepted_values and dbt_utils.expression_is_true across silver layer columns. Tests are applied at the silver layer only, enforcing data quality upstream ensures gold layer models inherit clean data. Testing downstream in gold would catch issues too late.

## Commands

```bash
dbt deps          # install packages listed in packages.yml
dbt run           # build all models in dependency order
dbt test          # run all data quality tests
dbt clean         # clear compiled SQL and run artifacts from target/
``
# projectA

This is an educational project to practice Python and its libraries.

The program prompts the user to select a geometric figure, choose between 2D or 3D, plots it and applies rotation (3D only). Figure coordinates are generated dynamically using numpy in `plot_engine.py`, no CSV needed. `main.py` handles user input and control flow, `constants.py` stores all static message strings, `logfile_generator.py` configures activity logging capturing info, warnings and errors throughout the session, and `session_logger.py` generates a JSON file per session containing plot metadata.

## How to run

```bash
python3 main.py  # macOS/Linux
python main.py   # Windows
```
Select a figure from the list when prompted, then select 2D or 3D.

## Libraries
- matplotlib
- numpy
- pandas
- logging (built-in)
- os (built-in)
- datetime (built-in)

## What's new?
Introduced JSON session logging. Each session generates a JSON file capturing figure name, triangle type, dimension, rotation, turn number and datetime per plot.

## What's next?

- Break `main.py` into multiple modules for better structure. 
- Create a PostgreSQL server, design the table schema, and send session JSON data to the database


## Long term vision

Make this an executable and build a data pipeline on top of it that logs all activity into a database using an orchestrator running on a scheduled job. Activity captured would include the plotting mode used, the figure selected or generated, and any other relevant metadata.


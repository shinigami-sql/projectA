# projectA

This is an educational project to practice Python and its libraries.

The program prompts the user to select a geometric figure and returns its corresponding data points. No plotting occurs yet, but the foundation is there. Data points are stored in `figures_datapoints.csv`, loaded in `figures.py` into a pandas DataFrame, and imported into `main.py` via `import figures`. It may seem like overkill to use pandas at this stage, but without using libraries in practice, learning cannot be achieved.

## How to run

```bash
python main.py
```

Select a figure from the list when prompted.

## What's next?

Plot figures in 2D and 3D with rotation applied, using `matplotlib`. Give the user the option to import their own CSV instead of using the built-in figures, and include the ability to generate a custom number of random data points and plot them.

## Long term vision

Make this an executable and build a data pipeline on top of it that logs all activity into a database using an orchestrator running on a scheduled job. Activity captured would include the plotting mode used, the figure selected or generated, and any other relevant metadata.

The goal is continuous improvement through building.
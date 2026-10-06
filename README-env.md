# DataKit environment exercise

This branch contains an environment-focused practice scenario.

## Setup

The project requires Python 3.12.

Use uv to create and synchronize the environment:

```bash
uv python install 3.12
uv sync --all-groups
```

Run the tests with:

```bash
uv run pytest
```

The command line entry point can be exercised with:

```bash
uv run datakit-summary data/example.json
```

The project also reads an optional environment variable:

```bash
DATAKIT_MIN_DEPTH=20
```

If the variable is not set, the default is 10.

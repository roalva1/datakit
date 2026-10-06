# datakit

A small Python toolkit for validating and transforming tabular records.

## Development

This branch contains an environment-focused practice scenario.

The project requires Python 3.12.

Set up the environment with uv, install the project dependencies, and run the test suite.

You should also verify that the command line entry point works against `data/example.json`.

The application supports an optional environment variable named `DATAKIT_MIN_DEPTH`. If it is not set, the default minimum depth is 10.

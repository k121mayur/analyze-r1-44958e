# Data Processing Application

This repository contains a Python application that processes data from an Excel file and outputs the results in JSON format.

## Setup Instructions
1. Ensure you have Python 3.11+ and Pandas 2.3 installed.
2. Run `python execute.py` to process the data.

## GitHub Actions
The repository includes a CI workflow that:
- Runs `ruff` to check for code quality.
- Executes `execute.py` to generate `result.json`.
- Publishes `result.json` via GitHub Pages.

## License
This project is licensed under the MIT License.
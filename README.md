# Baseball Scouting API

A FastAPI-based baseball scouting app that combines Sports Reference CSV source files, notebook-based data preparation, and a Jinja2 frontend to explore player stats by team and position.

## Overview

This project builds a scouting workflow from raw team CSV files through a cleaned master dataset and into a lightweight web application. The notebook prepares and merges the source files into `api_teams_data.csv`, while the FastAPI app serves a scouting page and an API endpoint for filtered player data.

## Features

- FastAPI backend for serving player data and page routes.
- Jinja2 template rendering through `templates/scout.html`.
- Team and position filtering through `POST /api/players`.
- Notebook-based data preparation in `lake.ipynb`.
- Cleaned aggregate dataset stored in `api_teams_data.csv`.
- Source CSV workflow using a `sources/` folder populated with Sports Reference exports.

## Project Structure

```bash
.
├── api.py
├── api_teams_data.csv
├── lake.ipynb
├── templates/
│   └── scout.html
└── sources/
    ├── braves.csv
    ├── dodgers.csv
    ├── yankees.csv
    └── ...
```

The FastAPI app points Jinja2 at the `templates` directory and renders `scout.html` from there. The raw team CSV files in `sources/` serve as the input layer for the notebook-based data pipeline.

## How It Works

1. Collect team CSV files from Sports Reference into the `sources/` folder.
2. Use `lake.ipynb` to load, clean, and merge those files.
3. Export the processed data to `api_teams_data.csv`.
4. Run `api.py` to serve the frontend and API endpoints.

## API Endpoints

### `GET /`

Renders the scouting interface using `templates/scout.html`.

### `POST /api/players`

Returns filtered player data using request fields such as team, position, and optional metrics.

Example request:

```json
{
  "team": "braves",
  "position": "1B",
  "metrics": ["WAR", "OPS", "HR"]
}
```

## Running the App

Install dependencies, then start the FastAPI development server:

```bash
uvicorn api:app --reload
```

Then open:

```bash
http://127.0.0.1:8000
```

## Tech Stack

- Python
- FastAPI
- pandas
- Jinja2
- HTML, CSS, and JavaScript

## Data Notes

The processed dataset includes player metrics such as team, age, position, WAR, OPS, OBP, SLG, HR, RBI, and related batting fields used for scouting-style filtering. The source workflow is designed around team-level Sports Reference CSV exports that are consolidated into a master table for application use.

## Future Improvements

- Add sorting by selected metrics.
- Add player name search.
- Add pagination or row limits for large result sets.
- Add richer scouting summaries and comparisons.
- Improve frontend styling and usability.

## License

Add a license here if you plan to publish the project publicly.

# Baseball Scouting API

A FastAPI-based baseball scouting app that combines Sports Reference CSV source files, notebook-based data preparation, and a Jinja2 frontend to explore player stats by team and position.

## Overview

This project builds a scouting workflow from raw team CSV files through a cleaned master dataset and into a lightweight web application.

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
    └── ...
```

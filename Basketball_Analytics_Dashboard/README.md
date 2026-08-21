# Basketball Analytics Dashboard

A simple web-based dashboard to view NBA player and team stats. Built with Flask, SQLite, Bootstrap 5, and Chart.js.

The app shows player stats through cards, charts, and a data table. Everything loads dynamically from the database via REST APIs.

## Features

- **Stats Cards** - Shows total players, teams, games, and average points
- **Top Scorers Chart** - Bar chart of the top 10 players by points
- **Position Breakdown** - Pie chart showing player distribution by position
- **Player Stats Table** - Full list of player stats sorted by points

All data comes from the database - no hardcoded values.

## Tech Stack

- **Backend**: Python & Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **UI Framework**: Bootstrap 5
- **Charts**: Chart.js
- **Font**: Google Poppins

## Project Structure

```
├── app.py                # Flask server
├── database.py           # Database setup script
├── requirements.txt      # Python packages
├── database/
│   └── nba.db           # SQLite database
├── templates/
│   └── index.html       # Dashboard page
└── static/
    ├── css/style.css    # Styling
    ├── js/script.js     # Frontend logic
    └── images/          # Assets
```

## Setup

1. Clone or extract this repo
2. Create a virtual environment (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

1. Set up the database
   ```bash
   python database.py
   ```
2. Start the server
   ```bash
   python app.py
   ```
3. Open your browser and go to `http://127.0.0.1:5000/`

## API Endpoints

- `GET /api/dashboard` - Stats for the KPI cards
- `GET /api/top-players` - Top 10 scorers
- `GET /api/player-position` - Players by position
- `GET /api/players` - Full player data

## To Do / Future Ideas

- Add filtering by team or position
- Search functionality for the player table
- Admin panel to manage data
- More visualizations (trends, comparisons, etc)
- Deploy to a cloud service

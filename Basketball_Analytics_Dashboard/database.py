"""
Database setup script for Basketball Analytics Dashboard
Creates SQLite database with sample NBA data
Run: python database.py
"""

import sqlite3
import os

# Make sure the "database" folder exists
DB_FOLDER = "database"
DB_PATH = os.path.join(DB_FOLDER, "nba.db")

if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)


def create_tables(cursor):
    """Create tables."""
    # Players
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            team TEXT NOT NULL,
            position TEXT NOT NULL,
            games INTEGER NOT NULL,
            points INTEGER NOT NULL,
            assists INTEGER NOT NULL,
            rebounds INTEGER NOT NULL,
            field_goal REAL NOT NULL
        )
    """)

    # Teams
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_name TEXT NOT NULL,
            conference TEXT NOT NULL,
            wins INTEGER NOT NULL,
            losses INTEGER NOT NULL
        )
    """)

    # Games
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            home_team TEXT NOT NULL,
            away_team TEXT NOT NULL,
            home_score INTEGER NOT NULL,
            away_score INTEGER NOT NULL,
            game_date TEXT NOT NULL
        )
    """)


def insert_players(cursor):
    """Insert sample player data."""

    players = [
        ("LeBron James", "Lakers", "Forward", 55, 1512, 429, 385, 52.4),
        ("Stephen Curry", "Warriors", "Guard", 56, 1428, 336, 246, 45.2),
        ("Kevin Durant", "Suns", "Forward", 54, 1458, 216, 351, 52.1),
        ("Giannis Antetokounmpo", "Bucks", "Forward", 58, 1734, 348, 638, 61.0),
        ("Nikola Jokic", "Nuggets", "Center", 57, 1596, 570, 690, 58.3),
        ("Joel Embiid", "76ers", "Center", 50, 1550, 200, 550, 53.6),
        ("Luka Doncic", "Mavericks", "Guard", 56, 1736, 476, 476, 48.7),
        ("Jayson Tatum", "Celtics", "Forward", 58, 1624, 261, 464, 46.5),
        ("Damian Lillard", "Bucks", "Guard", 55, 1540, 385, 220, 43.8),
        ("Devin Booker", "Suns", "Guard", 53, 1378, 371, 265, 47.9),
        ("Anthony Edwards", "Timberwolves", "Guard", 57, 1482, 285, 313, 45.6),
        ("Ja Morant", "Grizzlies", "Guard", 45, 1150, 337, 234, 46.8),
        ("Trae Young", "Hawks", "Guard", 54, 1350, 594, 205, 43.1),
        ("Jimmy Butler", "Heat", "Forward", 52, 1144, 260, 260, 49.5),
        ("Kawhi Leonard", "Clippers", "Forward", 48, 1152, 187, 230, 51.2),
        ("Paul George", "76ers", "Forward", 50, 1150, 200, 220, 44.7),
        ("Donovan Mitchell", "Cavaliers", "Guard", 55, 1512, 275, 220, 46.3),
        ("Bam Adebayo", "Heat", "Center", 56, 1120, 224, 616, 52.8),
        ("Domantas Sabonis", "Kings", "Center", 58, 1102, 464, 754, 60.1),
        ("Karl-Anthony Towns", "Knicks", "Center", 54, 1188, 216, 594, 50.9),
        ("De'Aaron Fox", "Kings", "Guard", 56, 1400, 336, 224, 47.6),
        ("Zion Williamson", "Pelicans", "Forward", 40, 960, 200, 240, 57.3),
        ("Shai Gilgeous-Alexander", "Thunder", "Guard", 57, 1710, 342, 285, 51.4),
        ("Anthony Davis", "Lakers", "Forward", 53, 1272, 159, 583, 55.9),
        ("Jaylen Brown", "Celtics", "Guard", 55, 1375, 220, 330, 48.9),
        ("Pascal Siakam", "Pacers", "Forward", 54, 1188, 216, 378, 49.1),
        ("Tyrese Haliburton", "Pacers", "Guard", 56, 1064, 616, 224, 47.8),
        ("Brandon Ingram", "Pelicans", "Forward", 44, 968, 220, 220, 46.9),
        ("Rudy Gobert", "Timberwolves", "Center", 58, 754, 116, 754, 65.2),
        ("Victor Wembanyama", "Spurs", "Center", 55, 1210, 220, 605, 46.5),
        ("Kyrie Irving", "Mavericks", "Guard", 52, 1300, 260, 208, 47.3),
        ("Klay Thompson", "Mavericks", "Guard", 54, 972, 108, 162, 44.8),
        ("Draymond Green", "Warriors", "Forward", 55, 550, 385, 385, 50.6),
        ("Chris Paul", "Spurs", "Guard", 53, 636, 477, 212, 46.1),
        ("Zach LaVine", "Kings", "Guard", 50, 1150, 200, 200, 45.0),
        ("Fred VanVleet", "Rockets", "Guard", 56, 952, 392, 168, 41.3),
        ("Jalen Brunson", "Knicks", "Guard", 57, 1596, 399, 171, 47.6),
        ("Alperen Sengun", "Rockets", "Center", 56, 1176, 336, 560, 53.4),
        ("Scottie Barnes", "Raptors", "Forward", 56, 1064, 336, 448, 47.9),
        ("Evan Mobley", "Cavaliers", "Center", 55, 990, 165, 550, 55.1),
    ]

    cursor.executemany("""
        INSERT INTO players
        (player_name, team, position, games, points, assists, rebounds, field_goal)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, players)


def insert_teams(cursor):
    """Insert sample team data."""

    teams = [
        ("Lakers", "Western", 47, 35),
        ("Warriors", "Western", 44, 38),
        ("Suns", "Western", 49, 33),
        ("Bucks", "Eastern", 51, 31),
        ("Nuggets", "Western", 53, 29),
        ("76ers", "Eastern", 46, 36),
        ("Mavericks", "Western", 50, 32),
        ("Celtics", "Eastern", 57, 25),
        ("Timberwolves", "Western", 52, 30),
        ("Grizzlies", "Western", 41, 41),
        ("Hawks", "Eastern", 38, 44),
        ("Heat", "Eastern", 45, 37),
        ("Clippers", "Western", 48, 34),
        ("Cavaliers", "Eastern", 54, 28),
        ("Kings", "Western", 46, 36),
        ("Knicks", "Eastern", 50, 32),
        ("Pelicans", "Western", 42, 40),
        ("Thunder", "Western", 56, 26),
        ("Pacers", "Eastern", 45, 37),
        ("Spurs", "Western", 39, 43),
        ("Rockets", "Western", 43, 39),
        ("Raptors", "Eastern", 33, 49),
    ]

    cursor.executemany("""
        INSERT INTO teams (team_name, conference, wins, losses)
        VALUES (?, ?, ?, ?)
    """, teams)


def insert_games(cursor):
    """Insert sample game data."""

    games = [
        ("Lakers", "Warriors", 118, 112, "2026-01-05"),
        ("Bucks", "Celtics", 109, 115, "2026-01-06"),
        ("Nuggets", "Suns", 121, 118, "2026-01-07"),
        ("76ers", "Knicks", 102, 108, "2026-01-08"),
        ("Mavericks", "Clippers", 130, 124, "2026-01-09"),
        ("Heat", "Cavaliers", 99, 105, "2026-01-10"),
        ("Timberwolves", "Kings", 112, 110, "2026-01-11"),
        ("Thunder", "Rockets", 128, 119, "2026-01-12"),
        ("Grizzlies", "Pelicans", 104, 101, "2026-01-13"),
        ("Hawks", "Pacers", 116, 120, "2026-01-14"),
        ("Spurs", "Raptors", 98, 94, "2026-01-15"),
        ("Warriors", "Suns", 111, 117, "2026-01-16"),
        ("Celtics", "Knicks", 122, 113, "2026-01-17"),
        ("Lakers", "Nuggets", 108, 114, "2026-01-18"),
        ("Bucks", "76ers", 119, 110, "2026-01-19"),
        ("Cavaliers", "Pacers", 105, 100, "2026-01-20"),
        ("Kings", "Clippers", 112, 109, "2026-01-21"),
        ("Rockets", "Mavericks", 101, 106, "2026-01-22"),
        ("Thunder", "Timberwolves", 124, 118, "2026-01-23"),
        ("Heat", "Hawks", 96, 92, "2026-01-24"),
    ]

    cursor.executemany("""
        INSERT INTO games
        (home_team, away_team, home_score, away_score, game_date)
        VALUES (?, ?, ?, ?, ?)
    """, games)


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Drop existing tables so the script can be re-run safely
    cursor.execute("DROP TABLE IF EXISTS players")
    cursor.execute("DROP TABLE IF EXISTS teams")
    cursor.execute("DROP TABLE IF EXISTS games")

    create_tables(cursor)
    insert_players(cursor)
    insert_teams(cursor)
    insert_games(cursor)

    conn.commit()
    conn.close()

    print(f"Database created successfully at: {DB_PATH}")
    print("Tables created: players, teams, games")
    print("Sample data inserted successfully.")


if __name__ == "__main__":
    main()

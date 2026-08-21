"""
Basketball Analytics Dashboard
Main Flask app and REST API
"""

from flask import Flask, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.path.join("database", "nba.db")


def get_db_connection():
    """Get database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# Routes
@app.route("/")
def index():
    return render_template("index.html")


# API: Dashboard stats
@app.route("/api/dashboard")
def api_dashboard():
    conn = get_db_connection()
    cursor = conn.cursor()

    total_players = cursor.execute("SELECT COUNT(*) FROM players").fetchone()[0]
    total_teams = cursor.execute("SELECT COUNT(*) FROM teams").fetchone()[0]
    total_games = cursor.execute("SELECT COUNT(*) FROM games").fetchone()[0]

    avg_points_row = cursor.execute("""
        SELECT AVG(points * 1.0 / games) FROM players WHERE games > 0
    """).fetchone()[0]
    avg_points = round(avg_points_row, 1) if avg_points_row else 0

    conn.close()

    return jsonify({
        "total_players": total_players,
        "total_teams": total_teams,
        "total_games": total_games,
        "avg_points": avg_points
    })


# API: Top scorers
@app.route("/api/top-players")
def api_top_players():
    conn = get_db_connection()
    cursor = conn.cursor()

    rows = cursor.execute("""
        SELECT player_name, points
        FROM players
        ORDER BY points DESC
        LIMIT 10
    """).fetchall()

    conn.close()

    labels = [row["player_name"] for row in rows]
    data = [row["points"] for row in rows]

    return jsonify({"labels": labels, "data": data})


# API: Player positions
@app.route("/api/player-position")
def api_player_position():
    conn = get_db_connection()
    cursor = conn.cursor()

    rows = cursor.execute("""
        SELECT position, COUNT(*) as total
        FROM players
        GROUP BY position
    """).fetchall()

    conn.close()

    # Normalize into the 4 required buckets
    counts = {"Guard": 0, "Forward": 0, "Center": 0, "Other": 0}
    for row in rows:
        pos = row["position"]
        if pos in counts:
            counts[pos] += row["total"]
        else:
            counts["Other"] += row["total"]

    return jsonify({
        "labels": list(counts.keys()),
        "data": list(counts.values())
    })


# API: All players
@app.route("/api/players")
def api_players():
    conn = get_db_connection()
    cursor = conn.cursor()

    rows = cursor.execute("""
        SELECT player_name, team, position, games, points, assists, rebounds, field_goal
        FROM players
        ORDER BY points DESC
    """).fetchall()

    conn.close()

    players = [dict(row) for row in rows]
    return jsonify(players)


if __name__ == "__main__":
    app.run(debug=True)

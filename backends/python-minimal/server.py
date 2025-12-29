#!/usr/bin/env python3
"""
Minimal Gamified Life Tracker API
~50 lines, SQLite backend, REST API

Usage:
    python server.py
    curl -X POST localhost:8000/log -d '{"activity":"workout"}'
"""

from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
DB = "life_xp.db"
XP = {"workout": 50, "meditation": 30, "reading": 30, "task": 15, "deep_work": 50, "meal": 20, "sleep": 25}

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY, activity TEXT, xp INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)""")

def get_stats():
    with sqlite3.connect(DB) as conn:
        total_xp = conn.execute("SELECT COALESCE(SUM(xp),0) FROM logs").fetchone()[0]
        return {"level": total_xp // 500 + 1, "xp": total_xp, "xp_to_next": 500 - (total_xp % 500)}

def get_streak(activity):
    with sqlite3.connect(DB) as conn:
        rows = conn.execute(
            "SELECT DATE(timestamp) FROM logs WHERE activity=? ORDER BY timestamp DESC",
            (activity,)).fetchall()
    streak, expected = 0, datetime.now().date()
    for (d,) in rows:
        if datetime.strptime(d, "%Y-%m-%d").date() == expected:
            streak += 1
            expected -= timedelta(days=1)
        else:
            break
    return streak

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    activity = data.get("activity", "task")
    xp = XP.get(activity, 15)
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO logs (activity, xp) VALUES (?, ?)", (activity, xp))
    stats = get_stats()
    return jsonify({"ack": f"+{xp} XP", "streak": get_streak(activity), **stats})

@app.route("/stats")
def stats():
    return jsonify(get_stats())

if __name__ == "__main__":
    init_db()
    app.run(port=8000)

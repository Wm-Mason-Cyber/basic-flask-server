#!/usr/bin/env python3
"""Create demo SQLite DB if missing (used by docker-compose entrypoint)."""
from pathlib import Path
import sqlite3


def db_file():
    root = Path(__file__).resolve().parents[1]
    d = root / 'data'
    d.mkdir(parents=True, exist_ok=True)
    return d / 'demo.db'


def init_db():
    f = db_file()
    if f.exists():
        print(f"DB already exists at {f}")
        return
    conn = sqlite3.connect(f)
    try:
        cur = conn.cursor()
        cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
        cur.executemany('INSERT INTO users(name) VALUES (?)', [('Alice',), ('Bob',)])
        conn.commit()
        print(f"Created demo DB at {f}")
    finally:
        conn.close()


if __name__ == '__main__':
    init_db()

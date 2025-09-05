from flask import Blueprint, render_template, request, jsonify, current_app
from .helpers import html_escape
import json
from pathlib import Path
import sqlite3

main_bp = Blueprint('main', __name__)


def data_dir() -> Path:
    """Return the Path to the data directory (project-root/data)."""
    # Use the package's parent directory as project root
    root = Path(__file__).resolve().parents[1]
    d = root / 'data'
    d.mkdir(parents=True, exist_ok=True)
    return d


def messages_file() -> Path:
    return data_dir() / 'messages.json'


def read_messages():
    f = messages_file()
    if not f.exists():
        return []
    try:
        with f.open('r', encoding='utf-8') as fh:
            return json.load(fh)
    except Exception:
        # If the file is malformed, return empty list (safe default)
        return []


def append_message(msg: str):
    msgs = read_messages()
    msgs.append({'msg': msg})
    f = messages_file()
    with f.open('w', encoding='utf-8') as fh:
        json.dump(msgs, fh)


def db_file() -> Path:
    """Return path to SQLite demo DB in data/"""
    root = Path(__file__).resolve().parents[1]
    d = root / 'data'
    d.mkdir(parents=True, exist_ok=True)
    return d / 'demo.db'


def init_db():
    """Create and seed the demo SQLite DB if it doesn't exist."""
    f = db_file()
    if f.exists():
        return
    conn = sqlite3.connect(f)
    try:
        cur = conn.cursor()
        cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
        # seed with two users
        cur.executemany('INSERT INTO users(name) VALUES (?)', [('Alice',), ('Bob',)])
        conn.commit()
    finally:
        conn.close()


@main_bp.route('/')
def index():
    """Index page with navigation."""
    return render_template('index.html')


@main_bp.route('/vulnerable_reflected')
def vulnerable_reflected():
    """Reflected XSS (vulnerable).

    This intentionally returns the raw `q` parameter into the template and the
    template will mark it as safe (no escaping) to illustrate a vulnerability.
    Do NOT use this pattern in production.
    """
    q = request.args.get('q', '')
    return render_template('reflected.html', q=q, safe=False)


@main_bp.route('/safe_reflected')
def safe_reflected():
    """Reflected XSS (safe).

    This version relies on Jinja2 auto-escaping (or explicit escaping) so the
    user-supplied `q` is not executed as HTML.
    """
    q = request.args.get('q', '')
    return render_template('reflected.html', q=q, safe=True)


@main_bp.route('/stored_vuln', methods=['GET', 'POST'])
def stored_vuln():
    """Stored XSS demo (vulnerable).

    Stores messages to `data/messages.json` and displays them WITHOUT escaping
    so scripts in messages will be rendered by the browser (intentional).
    """
    if request.method == 'POST':
        msg = request.form.get('msg', '')
        append_message(msg)
    msgs = read_messages()
    # Pass messages to template; template will mark them as safe to show vulnerability
    return render_template('stored.html', messages=msgs, safe=False)


@main_bp.route('/stored_safe', methods=['GET', 'POST'])
def stored_safe():
    """Stored XSS demo (safe).

    Stores messages and displays them escaped to prevent execution.
    """
    if request.method == 'POST':
        msg = request.form.get('msg', '')
        append_message(msg)
    msgs = read_messages()
    # The template will display messages without marking safe, so Jinja escapes them
    return render_template('stored.html', messages=msgs, safe=True)


@main_bp.route('/api/search')
def api_search():
    """Simple API endpoint that returns raw and escaped query values."""
    q = request.args.get('q', '')
    return jsonify({'raw': q, 'escaped': html_escape(q)})


@main_bp.route('/sql_vuln')
def sql_vuln():
    """SQLi vulnerable endpoint: builds SQL query using string concatenation.

    This demonstrates why concatenating user input into SQL is dangerous.
    """
    name = request.args.get('name', '')
    init_db()
    dbp = db_file()
    conn = sqlite3.connect(dbp)
    try:
        cur = conn.cursor()
        # Intentionally vulnerable: concatenate user input directly into SQL
        query = f"SELECT id, name FROM users WHERE name = '{name}'"
        cur.execute(query)
        rows = cur.fetchall()
    finally:
        conn.close()
    # render simple list
    return render_template('sql.html', rows=rows, vuln=True, query=query)


@main_bp.route('/sql_safe')
def sql_safe():
    """Safe SQL endpoint: uses parameterized queries."""
    name = request.args.get('name', '')
    init_db()
    dbp = db_file()
    conn = sqlite3.connect(dbp)
    try:
        cur = conn.cursor()
        # Parameterized query prevents SQL injection
        cur.execute('SELECT id, name FROM users WHERE name = ?', (name,))
        rows = cur.fetchall()
    finally:
        conn.close()
    return render_template('sql.html', rows=rows, vuln=False, query=None)

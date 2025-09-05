# Flask Basics Demo

![CI](https://github.com/Wm-Mason-Cyber/basic-flask-server/actions/workflows/ci.yml/badge.svg)

A simple Flask app for teaching web basics and security concepts (XSS, SQLi, API safety).

> WARNING: This repo intentionally contains vulnerable code for classroom use. Do not deploy to public servers.

Quickstart

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run locally
export FLASK_APP=app:create_app
flask run
```

Run tests

```bash
source venv/bin/activate
PYTHONPATH=. pytest -q
```

Run with Docker Compose

```bash
docker compose up --build
```

Reset demo data

```
bash scripts/reset_data.sh
```

See `docs/WORKSHEET.md` for lab steps and the instructor answer key.

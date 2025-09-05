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

## Technologies used

Below are the logos of the main technologies used in this project to help students recognize them.

<p align="left">
	<img alt="Python" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" height="72" />
	<img alt="Flask" src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" height="72" />
	<img alt="SQLite" src="https://upload.wikimedia.org/wikipedia/commons/3/38/SQLite370.svg" height="72" />
	<img alt="Docker" src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Docker_%28container_engine%29_logo.svg" height="72" />
</p>

Release v0.1.0 — initial classroom scaffold

Date: 2025-09-04

Summary
-------
Initial release of a minimal Flask classroom demo that demonstrates reflected XSS, stored XSS, SQL injection, and a tiny API for teaching web security basics. The repository is intentionally educational and contains vulnerable code for classroom use only.

Highlights
----------
- Reflected XSS demo: `/vulnerable_reflected` (vulnerable) and `/safe_reflected` (safe)
- Stored XSS demo: `/stored_vuln` (stores and renders unescaped) and `/stored_safe` (stores and escapes)
- SQLi demo: `/sql_vuln` (string-concatenated query) and `/sql_safe` (parameterized)
- Small JSON storage in `data/messages.json` and SQLite at `data/demo.db` (both gitignored)
- Tests: pytest suite covering reflected/stored XSS, API, and SQLi behaviors
- Docker: `Dockerfile` and `docker-compose.yml` with init script to create/seed DB
- CI: GitHub Actions workflow to run tests
- Docs: student worksheet, project goals, test plan, and runbook

Important safety note
---------------------
This project contains purposely vulnerable code for teaching. Do not deploy this to public servers. Run it on isolated machines or VMs and reset data between student runs with `bash scripts/reset_data.sh`.

Files changed in this release (high level)
-----------------------------------------
- Added app code under `app/` (create_app, routes, helpers, templates)
- Added tests under `tests/` (pytest)
- Added `docs/` with a beginner-friendly worksheet and instructor answers
- Added `Dockerfile`, `docker-compose.yml`, and `scripts/init_db.py`

How to get started
------------------
1. Clone the repo and checkout `v0.1.0`:

   git clone https://github.com/Wm-Mason-Cyber/basic-flask-server.git
   cd basic-flask-server
   git checkout v0.1.0

2. Run locally (quick):

   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   export FLASK_APP=app:create_app
   flask run

3. Open the student worksheet `docs/WORKSHEET.md` and follow the exercises.

Notes for maintainers
---------------------
- Tests run quickly with the Flask test client; CI runs them on push.
- If adding new exercises, include a test demonstrating the vulnerable vs safe behavior.
- Consider adding a GitHub Release via the web UI to attach this release notes text and mark the release as published.

Acknowledgements
----------------
Author: Classroom Demo
License: MIT

Patch v0.1.1 — small fixes and styling update

Date: 2025-09-05

Changes
-------
- Removed obsolete `version` key from `docker-compose.yml` and added a lightweight container healthcheck.
- Updated front-end stylesheet to a flexbox-driven, high-contrast modern theme for better accessibility and readability.

How to verify
-------------
1. Build and run the app locally with Docker Compose and check the health status:

   docker compose up --build

2. Run the test suite locally:

   PYTHONPATH=. pytest -q

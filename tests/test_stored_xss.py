from app import create_app
import os
from pathlib import Path


def test_stored_vuln_and_safe(tmp_path, monkeypatch):
    # Ensure data dir points to tmp_path/data by creating the folder structure
    project_root = tmp_path
    data_dir = project_root / 'data'
    data_dir.mkdir()

    # Monkeypatch Path resolution in routes.data_dir by setting __file__ parent
    # We'll monkeypatch the package file path so data_dir() uses tmp_path
    import app.routes as routes
    real_file = routes.__file__
    try:
        # Temporarily set __file__ to inside tmp_path/package/app/routes.py
        routes.__file__ = str(project_root / 'pkg' / 'app' / 'routes.py')
        app = create_app()
        client = app.test_client()

        payload = '<script>alert(1)</script>'
        # Post to stored_vuln
        r = client.post('/stored_vuln', data={'msg': payload}, follow_redirects=True)
        assert r.status_code == 200
        body = r.get_data(as_text=True)
        assert payload in body

        # Post to stored_safe
        payload2 = '<img src=x onerror=alert(2)>'
        r = client.post('/stored_safe', data={'msg': payload2}, follow_redirects=True)
        assert r.status_code == 200
        body = r.get_data(as_text=True)
        # safe version should escape angle brackets, so raw '<img' shouldn't appear
        assert '<img' not in body
    finally:
        routes.__file__ = real_file

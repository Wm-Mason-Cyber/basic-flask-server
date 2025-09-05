import json
import html
from pathlib import Path

from app import create_app


def test_api_escape_matches_html_escape():
    app = create_app()
    client = app.test_client()

    payload = '<b>bold</b>'
    r = client.get(f'/api/search?q={payload}')
    assert r.status_code == 200
    data = json.loads(r.get_data(as_text=True))
    assert data['raw'] == payload
    assert data['escaped'] == html.escape(payload)


def test_stored_persists_to_messages_json(tmp_path):
    # Prepare a fake project layout so routes.data_dir() writes into tmp_path/data
    project_root = tmp_path
    data_dir = project_root / 'data'
    data_dir.mkdir()

    import app.routes as routes
    real_file = routes.__file__
    try:
        routes.__file__ = str(project_root / 'pkg' / 'app' / 'routes.py')
        app = create_app()
        client = app.test_client()

        payload = 'persist-me'
        r = client.post('/stored_vuln', data={'msg': payload})
        assert r.status_code == 200

        # Determine the messages file used by the app (routes.messages_file())
        mf = routes.messages_file()
        assert mf.exists()
        content = json.loads(mf.read_text(encoding='utf-8'))
        assert any(entry.get('msg') == payload for entry in content)
    finally:
        routes.__file__ = real_file

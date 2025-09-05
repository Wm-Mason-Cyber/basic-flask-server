import json
from app import create_app


def test_index_returns_200():
    app = create_app()
    client = app.test_client()

    r = client.get('/')
    assert r.status_code == 200


def test_api_search_echoes():
    app = create_app()
    client = app.test_client()

    r = client.get('/api/search?q=hello')
    assert r.status_code == 200
    data = json.loads(r.data)
    assert data['raw'] == 'hello'
    assert 'escaped' in data

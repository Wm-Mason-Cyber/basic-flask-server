from app import create_app


def test_vulnerable_reflected_shows_payload():
    app = create_app()
    client = app.test_client()

    payload = '<script>alert(1)</script>'
    r = client.get(f'/vulnerable_reflected?q={payload}')
    assert payload in r.get_data(as_text=True)


def test_safe_reflected_escapes_payload():
    app = create_app()
    client = app.test_client()

    payload = '<script>alert(1)</script>'
    r = client.get(f'/safe_reflected?q={payload}')
    body = r.get_data(as_text=True)
    # the safe page should not contain the raw script tag
    assert '<script>' not in body

from app import create_app
import re
import html


def test_sql_vuln_injection():
    app = create_app()
    client = app.test_client()

    # Use a payload that, when concatenated, will always be true and return rows
    payload = "' OR '1'='1"
    r = client.get(f'/sql_vuln?name={payload}')
    assert r.status_code == 200
    body = r.get_data(as_text=True)
    # vulnerable page should indicate VULNERABLE MODE and return seeded users
    assert 'VULNERABLE MODE' in body
    assert re.search(r'Alice|Bob', body)


def test_sql_safe_prevents_injection():
    app = create_app()
    client = app.test_client()

    payload = "' OR '1'='1"
    r = client.get(f'/sql_safe?name={payload}')
    assert r.status_code == 200
    body = r.get_data(as_text=True)
    # safe page should not indicate vulnerability and should not return seeded users
    assert 'VULNERABLE MODE' not in body
    assert not re.search(r'Alice|Bob', body)

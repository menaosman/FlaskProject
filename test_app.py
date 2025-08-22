import json
from flask_demo import app

def test_health_route():
    client = app.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data.get('status') == 'ok'


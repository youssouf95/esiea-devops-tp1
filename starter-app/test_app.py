import fakeredis
import redis

import app as app_module
from app import alert_threshold, sanitize_input, app


def test_alert_threshold():
    assert alert_threshold() == 25


def test_sanitize_input_escapes_html():
    assert sanitize_input("<script>") == "&lt;script&gt;"


def test_health_endpoint(monkeypatch):
    fake_client = fakeredis.FakeStrictRedis(decode_responses=True)

    def fake_get_redis_client():
        return fake_client

    monkeypatch.setattr(app_module, "get_redis_client", fake_get_redis_client)

    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_health_endpoint_redis_down(monkeypatch):
    class BrokenClient:
        def ping(self):
            raise redis.exceptions.ConnectionError("redis down")

    def fake_get_redis_client():
        return BrokenClient()

    monkeypatch.setattr(app_module, "get_redis_client", fake_get_redis_client)

    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 503


def test_status_endpoint():
    client = app.test_client()
    response = client.get("/status")
    assert response.status_code == 200
    assert response.get_json()["service"] == "projet-devops-groupe-demo"


def test_visits_endpoint_increments(monkeypatch):
    fake_client = fakeredis.FakeStrictRedis(decode_responses=True)

    def fake_get_redis_client():
        return fake_client

    monkeypatch.setattr(app_module, "get_redis_client", fake_get_redis_client)

    client = app.test_client()
    first = client.get("/visits").get_json()["visits"]
    second = client.get("/visits").get_json()["visits"]

    assert second == first + 1

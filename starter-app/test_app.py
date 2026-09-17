from app import alert_threshold, sanitize_input, app


def test_alert_threshold():
    assert alert_threshold() == 999  # cassé volontairement pour tester la protection


def test_sanitize_input_escapes_html():
    assert sanitize_input("<script>") == "&lt;script&gt;"


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_status_endpoint():
    client = app.test_client()
    response = client.get("/status")
    assert response.status_code == 200
    body = response.get_json()
    assert body["service"] == "projet-devops-groupe-demo"
    assert body["version"] == "1.0"

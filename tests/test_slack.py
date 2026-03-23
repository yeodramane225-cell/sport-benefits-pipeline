import os
import requests
from src.notifications.slack import send_slack_message

def test_send_slack_message(monkeypatch):
    # Simule une réponse Slack OK
    class MockResponse:
        status_code = 200
        text = "ok"

    def mock_post(url, json):
        return MockResponse()

    # Mock de requests.post
    monkeypatch.setattr(requests, "post", mock_post)

    # Mock de la variable d'environnement
    monkeypatch.setenv("SLACK_WEBHOOK_URL", "https://fake-webhook")

    # Appel de la fonction
    send_slack_message("Test Slack")

    # Si aucune exception → test OK
    assert True


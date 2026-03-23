import requests
import os

def send_slack_message(message: str):
    """
    Envoie un message Slack via un webhook.
    """
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")

    if not webhook_url:
        raise ValueError("SLACK_WEBHOOK_URL non défini dans les variables d'environnement.")

    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)

    if response.status_code != 200:
        raise RuntimeError(f"Erreur Slack : {response.text}")


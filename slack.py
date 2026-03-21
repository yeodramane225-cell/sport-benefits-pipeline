import requests
import pandas as pd
from src.config.settings import SLACK_WEBHOOK

def notify_new_activities():
    df = pd.read_csv("/tmp/processed.csv")
    for _, row in df.iterrows():
        msg = f"{row['name']} a fait une activité : {row['type']} - {row['distance_km']} km"
        requests.post(SLACK_WEBHOOK, json={"text": msg})


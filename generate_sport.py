from faker import Faker
import pandas as pd
import boto3
from src.config.settings import *

def generate_sport():
    fake = Faker()
    data = []

    for i in range(50):
        data.append({
            "employee_id": fake.random_int(1, 20),
            "date": fake.date_this_month(),
            "type": fake.random_element(["run", "bike", "walk"]),
            "distance_km": fake.random_int(1, 20),
            "duration_min": fake.random_int(10, 120),
            "commute": fake.boolean()
        })

    df = pd.DataFrame(data)

    s3 = boto3.client(
        "s3",
        endpoint_url=S3_ENDPOINT,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY
    )

    s3.put_object(
        Bucket=S3_BUCKET,
        Key="raw/sport/sport.csv",
        Body=df.to_csv(index=False)
    )


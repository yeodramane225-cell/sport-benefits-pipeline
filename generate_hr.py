from faker import Faker
import pandas as pd
import boto3
from src.config.settings import *

def generate_hr():
    fake = Faker()
    data = []

    for i in range(20):
        data.append({
            "employee_id": i+1,
            "name": fake.name(),
            "salary": fake.random_int(35000, 70000),
            "site": fake.city()
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
        Key="raw/hr/hr.csv",
        Body=df.to_csv(index=False)
    )


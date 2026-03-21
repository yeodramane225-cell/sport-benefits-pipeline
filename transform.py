import pandas as pd
import boto3
from src.config.settings import *
from src.processing.rules import *

def run_transform():
    s3 = boto3.client(
        "s3",
        endpoint_url=S3_ENDPOINT,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY
    )

    hr = pd.read_csv(s3.get_object(Bucket=S3_BUCKET, Key="raw/hr/hr.csv")["Body"])
    sport = pd.read_csv(s3.get_object(Bucket=S3_BUCKET, Key="raw/sport/sport.csv")["Body"])

    df = sport.merge(hr, on="employee_id")

    df = compute_prime_eligibility(df)
    df = compute_bien_etre(df)

    df.to_csv("/tmp/processed.csv", index=False)


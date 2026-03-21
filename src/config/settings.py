import os

S3_ENDPOINT = "http://minio:9000"
S3_ACCESS_KEY = "admin"
S3_SECRET_KEY = "admin123"
S3_BUCKET = "sport-benefits"

POSTGRES_CONN = "postgresql://kestra:kestra@postgres:5432/sportdb"

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

PRIME_RATE = float(os.getenv("PRIME_RATE", 0.05))


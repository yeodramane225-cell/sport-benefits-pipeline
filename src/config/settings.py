import os

# ============================
# MinIO (S3-like)
# ============================
S3_ENDPOINT = os.getenv("S3_ENDPOINT", "http://localhost:9000")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY", "admin")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY", "admin123")

# Ton bucket réel dans MinIO
S3_BUCKET = os.getenv("S3_BUCKET", "raw")

# ============================
# PostgreSQL
# ============================
POSTGRES_CONN = os.getenv(
    "POSTGRES_CONN",
    "postgresql://kestra:kestra@postgres:5432/sportdb"
)

# ============================
# Slack
# ============================
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

# ============================
# Variables métier
# ============================
PRIME_RATE = float(os.getenv("PRIME_RATE", 0.05))

# ============================
# Faker (génération de données)
# ============================
FAKER_HR_OUTPUT = os.getenv("FAKER_HR_OUTPUT", "hr_generated.csv")
FAKER_SPORT_OUTPUT = os.getenv("FAKER_SPORT_OUTPUT", "sport_generated.csv")


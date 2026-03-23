from config.settings import (
    S3_ENDPOINT, S3_ACCESS_KEY, S3_SECRET_KEY,
    POSTGRES_CONN, SLACK_WEBHOOK, PRIME_RATE,
    FAKER_HR_OUTPUT, FAKER_SPORT_OUTPUT
)

def test_minio_config():
    assert all([S3_ENDPOINT, S3_ACCESS_KEY, S3_SECRET_KEY])

def test_postgres_config():
    assert POSTGRES_CONN is not None

def test_slack_config():
    assert SLACK_WEBHOOK is not None

def test_business_variables():
    assert PRIME_RATE is not None

def test_faker_config():
    assert FAKER_HR_OUTPUT is not None
    assert FAKER_SPORT_OUTPUT is not None


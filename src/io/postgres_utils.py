import pandas as pd
from sqlalchemy import create_engine


def load_to_postgres(df: pd.DataFrame, table_name: str):
    """
    Charge un DataFrame dans une table Postgres.
    """
    # Connexion Postgres (selon ton docker-compose)
    engine = create_engine("postgresql://kestra:kestra@localhost:5432/sportdb")

    # Insertion dans la table
    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )


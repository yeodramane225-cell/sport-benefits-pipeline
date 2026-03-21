import pandas as pd
from sqlalchemy import create_engine
from src.config.settings import *

def load_to_postgres():
    df = pd.read_csv("/tmp/processed.csv")
    engine = create_engine(POSTGRES_CONN)
    df.to_sql("benefits", engine, if_exists="replace", index=False)


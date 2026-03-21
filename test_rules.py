import pandas as pd
from src.processing.rules import *

def test_prime():
    df = pd.DataFrame({"employee_id":[1,1,1,1,1], "commute":[1,1,1,1,1]})
    df = compute_prime_eligibility(df)
    assert df["eligible_prime"].iloc[0] == True


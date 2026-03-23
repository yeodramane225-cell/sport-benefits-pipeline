import pandas as pd
from great_expectations.dataset import PandasDataset

def test_great_expectations():
    df = pd.read_csv("sport_generated.csv")
    ge_df = PandasDataset(df)

    # 1. employee_id non nul
    assert ge_df.expect_column_values_to_not_be_null("employee_id").success

    # 2. dates valides
    assert ge_df.expect_column_values_to_match_strftime_format(
        "date", "%Y-%m-%d"
    ).success

    # 3. distances >= 0 si la colonne existe
    if "distance_km" in ge_df.columns:
        assert ge_df.expect_column_values_to_be_between(
            "distance_km", min_value=0
        ).success


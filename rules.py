def compute_prime_eligibility(df):
    df["eligible_prime"] = df["commute"].astype(int).groupby(df["employee_id"]).transform("sum") >= 5
    return df

def compute_bien_etre(df):
    df["eligible_bien_etre"] = df["distance_km"].groupby(df["employee_id"]).transform("sum") >= 50
    return df


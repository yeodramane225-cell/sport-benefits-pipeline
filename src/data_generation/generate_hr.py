import pandas as pd
from faker import Faker
import random

fake = Faker("fr_FR")

def generate_hr_data(n=100):
    data = []
    for i in range(1, n + 1):
        data.append({
            "employee_id": i,
            "nom": fake.last_name(),
            "prenom": fake.first_name(),
            "date_embauche": fake.date_between(start_date="-10y", end_date="today"),
            "anciennete": random.randint(0, 10),
            "departement": fake.random_element(["IT", "RH", "Finance", "Marketing"]),
            "distance_km": round(random.uniform(1, 50), 2)
        })
    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_hr_data(100)
    df.to_csv("hr_generated.csv", index=False)
    print("✔️ Données RH générées : hr_generated.csv")


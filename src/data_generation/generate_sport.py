import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker("fr_FR")

def generate_sport_data(n_employees=100, months=12):
    data = []
    today = datetime.today()

    for emp_id in range(1, n_employees + 1):
        for m in range(months):
            date_activity = today - timedelta(days=30 * m)
            data.append({
                "employee_id": emp_id,
                "date": date_activity.date(),
                "activite_sportive": random.randint(0, 20),  # nb séances/mois
                "type_activite": fake.random_element(["Running", "Cycling", "Yoga", "Natation", "Fitness"]),
                "duree_totale_min": random.randint(30, 600)
            })

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_sport_data(100, 12)
    df.to_csv("sport_generated.csv", index=False)
    print("✔️ Données sportives générées : sport_generated.csv")


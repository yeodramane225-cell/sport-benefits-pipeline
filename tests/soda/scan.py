from soda.scan import Scan

scan = Scan()

# Déclare la data source pandas
scan.set_data_source_name("pandas")

# Charge ton CSV
scan.add_pandas_file("sport_generated.csv")

# Ajoute les checks (SODA v4 accepte ce format dans une string Python)
scan.add_check("""
checks for sport_generated:
  - invalid_count(distance_km) = 0:
      valid_min: 0
  - invalid_count(date) = 0:
      valid_format: "%Y-%m-%d"
  - missing_count(employee_id) = 0
""")

scan.execute()


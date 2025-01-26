import csv
import random

# Define the output file name
output_file = "demo_data.csv"

# Number of rows to generate
num_rows = 1000

# Define ranges for random data generation
data_ranges = {
    "temprature-zone1": (25.0, 35.0),
    "temprature-zone2": (30.0, 40.0),
    "humidity-zone1": (45.0, 55.0),
    "humidity-zone2": (35.0, 45.0),
    "light1-zone1": (20.0, 50.0),
    "light2-zone1": (30.0, 60.0),
    "water-zone1": (90.0, 110.0),
    "feed-zone1": (80.0, 100.0),
}

# Column names
columns = list(data_ranges.keys())

# Generate data
rows = [
    {
        col: round(random.uniform(*data_ranges[col]), 2)
        for col in columns
    }
    for _ in range(num_rows)
]

# Write to CSV
with open(output_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)

print(f"Dummy data has been saved to {output_file}")

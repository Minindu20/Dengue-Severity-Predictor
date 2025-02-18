import pandas as pd
import json

# Load CSV file
df = pd.read_csv("final_combined_dataset.csv")

# Ensure the dataset has relevant columns (adjust column names if needed)
geocode_column = "geocode"  # Change if your column name is different
cases_column = "cases"  # Change if your column name is different

# Group by geocode and sum up the total cases
total_cases = df.groupby(geocode_column)[cases_column].sum()

# Normalize values between 0 and 1 using Min-Max scaling
min_cases = total_cases.min()
max_cases = total_cases.max()
normalized_cases = (total_cases - min_cases) / (max_cases - min_cases)

# Convert to dictionary
normalized_cases_dict = normalized_cases.to_dict()

# Save to JSON
output_file = "total_cases_by_geocode.json"
with open(output_file, "w") as json_file:
    json.dump(normalized_cases_dict, json_file, indent=4)

print(f"JSON file saved: {output_file}")
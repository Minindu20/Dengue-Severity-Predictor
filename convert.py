import pandas as pd
import json

# Read the CSV file into a DataFrame
df = pd.read_csv('52_week_dengue_dataset.csv')

# Ensure the columns 'date' and 'cases' exist
df['years'] = df['week'].astype(str).str[:4].astype(int)
df['weeks'] = df['week'].astype(str).str[4:6].astype(int)

# Group by 'year' and 'week' and sum the 'cases'
grouped = df.groupby(['years', 'weeks'])['cases'].sum().reset_index()

# Create a dictionary to hold the final structure
result = {}

# Populate the result dictionary
for _, row in grouped.iterrows():
    year = int(row['years'])
    week = f"Week {row['weeks']}"
    cases = int(row['cases'])

    if year not in result:
        result[year] = {}

    result[year][week] = cases

# Save the result to a JSON file
with open('dengue-cases.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)

print("Data has been successfully processed and saved to output.json.")

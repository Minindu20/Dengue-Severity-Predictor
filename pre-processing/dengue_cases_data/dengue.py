import pandas as pd

file_path = 'output/converted_csv_file.csv'

# Using error_bad_lines=False to skip rows with mismatched columns
df = pd.read_csv(file_path, usecols=range(81))

filtered_df = df[df['STATE'] == 'RJ'][['CITY', 'STATE', 'LONG', 'LAT', 'ALT']]
filtered_df.to_csv('filtered_RJ_lat_long_data.dengue_cases_data', index=False)

print("Filtered data has been saved to filtered_RJ_lat_long_data.dengue_cases_data")

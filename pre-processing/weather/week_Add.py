import pandas as pd

def add_week_column(out_tempo_path, dates_path, output_path):
    # Read the CSV files
    out_tempo = pd.read_csv(out_tempo_path)
    dates = pd.read_csv(dates_path)

    # Convert dates to datetime for comparison
    out_tempo['DATA'] = pd.to_datetime(out_tempo['DATA'], errors='coerce')  # Ensure any invalid dates are turned into NaT
    dates['start_date'] = pd.to_datetime(dates['start_date'], errors='coerce')
    dates['end_date'] = pd.to_datetime(dates['end_date'], errors='coerce')

    print("Function started")

    # Initialize a new column 'week' with NaN
    out_tempo['week'] = None

    # Add 'week' values based on the date range
    for i, row in dates.iterrows():
        print(f"Checking week: {row['week']} from {row['start_date']} to {row['end_date']}")
        # Make sure the mask condition is valid and matches data
        mask = (out_tempo['DATA'] >= row['start_date']) & (out_tempo['DATA'] <= row['end_date'])
        matched_rows = out_tempo.loc[mask]
        print(f"Matched {len(matched_rows)} rows")

        # Assign the week value
        out_tempo.loc[mask, 'week'] = row['week']

    # Drop rows with NaN values in the 'week' column
    out_tempo_cleaned = out_tempo.dropna(subset=['week'])

    # Check how many NaN values remain
    nan_count = out_tempo_cleaned['week'].isna().sum()
    print(f"Number of NaN values in the 'week' column after dropping: {nan_count}")

    # Save the cleaned DataFrame to a new CSV file
    out_tempo_cleaned.to_csv(output_path, index=False)

# Usage
add_week_column('data/filled_rain_data.csv', 'data/dates.csv', 'data/updated_out_tempo5.csv')

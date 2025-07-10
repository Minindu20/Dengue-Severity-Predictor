import pandas as pd
import json

# Read CSV file
df = pd.read_csv("final_combined_dataset.csv")

# Define the weather parameters and their corresponding JSON keys
weather_params = {
    "tempe_min": "Minimum Temperature",
    "precipitation_avg_regression_kriging": "Average Precipitation",
    "humidity_max": "Maximum Humidity"
}  # Add more as needed

# Create the JSON structure
weather_json = {}

for _, row in df.iterrows():
    geocode = str(row["geocode"])  # Convert geocode to string for JSON key
    year = str(row["week"])[:4]  # Extract year from YYYYWW
    week_number = int(str(row["week"])[4:])  # Extract week number from YYYYWW
    week_key = f"Week {week_number}"  # Format as "Week X"

    if geocode not in weather_json:
        weather_json[geocode] = {}
    if year not in weather_json[geocode]:
        weather_json[geocode][year] = {}

    # Store multiple weather parameters for the week with actual labels
    weather_json[geocode][year][week_key] = {
        label: row[param] for param, label in weather_params.items() if param in df.columns
    }

# Save to a JSON file
with open("weather_data.json", "w") as f:
    json.dump(weather_json, f, indent=4)

print("JSON file saved as weather_data.json")
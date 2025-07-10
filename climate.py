import pandas as pd
import json

# Read the CSV file
df = pd.read_csv('a.csv')

# ---------- Part 1: Week 202217 JSON Output ----------
week_df = df[df['week'] == 202219]

# Create dictionary: {geocode: ensemble_pred}
result_dict = dict(zip(week_df['geocode'], week_df['ensemble_pred']))

# Save JSON (optional)
with open('output.json', 'w') as f:
    json.dump(result_dict, f, indent=2)

# Print the JSON
print("JSON Output for week 202217:")
print(json.dumps(result_dict, indent=2))

# ---------- Part 2: Value Buckets ----------
buckets = {
    "<1": [],
    "1-10": [],
    "10-30": [],
    "30-50": [],
    "50-100": [],
    "100+": []
}

for geocode, value in result_dict.items():
    if value < 1:
        buckets["<1"].append((geocode, value))
    elif value < 10:
        buckets["1-10"].append((geocode, value))
    elif value < 30:
        buckets["10-30"].append((geocode, value))
    elif value < 50:
        buckets["30-50"].append((geocode, value))
    elif value < 100:
        buckets["50-100"].append((geocode, value))
    else:
        buckets["100+"].append((geocode, value))

# Print summary counts
print("\nValue Distribution Summary for week 202217:")
for range_label, entries in buckets.items():
    print(f"{range_label}: {len(entries)} values")

# ---------- Part 3: Week(s) with most ensemble_pred > 10 ----------
greater_than_10_df = df[df['ensemble_pred'] > 10]
week_counts = greater_than_10_df.groupby('week').size()

if not week_counts.empty:
    max_count = week_counts.max()
    weeks_with_max = week_counts[week_counts == max_count].index.tolist()

    print(f"\nWeek(s) with the highest number of ensemble_pred > 10: {weeks_with_max}")
    print(f"Maximum count: {max_count}")
else:
    print("\nNo ensemble_pred values greater than 10 found in any week.")
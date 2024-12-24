import pandas as pd

file_path = 'dengue_cases_data/input/br_vegetation.dengue_cases_data'
df = pd.read_csv(file_path)

df['ADM2_PCODE'] = df['ADM2_PCODE'].str.replace('BR', '')
df = df.rename(columns={'ADM2_PCODE': 'geocode'})

filtered_df = df[df['geocode'].str.startswith('33')]
filtered_df.to_csv('Br_RJ_Vegetation_Converted.dengue_cases_data', index=False)

print("BR prefix removed, column renamed to 'geocode', and data saved to modified_file.dengue_cases_data")

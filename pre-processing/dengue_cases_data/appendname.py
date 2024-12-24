import pandas as pd

filtered_file = 'output/Br_RJ_Vegetation_Converted.csv'
filtered_df = pd.read_csv(filtered_file)

file_path = 'output/filtered_RJ_cities.csv'
fileA_df = pd.read_csv(file_path)

columns = ['date', 'name', 'geocode', 'vim', 'vim_avg', 'viq']

merged_df = pd.merge(filtered_df, fileA_df[['name', 'idIBGE']], left_on='geocode', right_on='idIBGE', how='left')

merged_df = merged_df.drop(columns=['idIBGE'])

merged_df = merged_df[columns]

merged_df.to_csv('Br_vegetation_with_City.dengue_cases_data', index=False)

print("City names added based on geocode, and data saved to filtered_with_city.dengue_cases_data")

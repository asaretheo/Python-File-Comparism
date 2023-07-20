import pandas as pd

# Load Data A and Data B CSV files
data_a = pd.read_csv('data_a.csv')
data_b = pd.read_csv('data_b.csv')

# Get unique identifiers from Data A
unique_identifiers = data_a['Identifier'].unique()

# Initialize a list to store the results
results = []

# Search for matches in Data B
for identifier in unique_identifiers:
    match = data_b[data_b['Identifier'] == identifier]
    if not match.empty:
        area_of_residence = match['Area of residence'].values[0]
        results.append([identifier, area_of_residence])

# Create a new DataFrame from the results
result_df = pd.DataFrame(results, columns=['Identifier', 'Area of Residence'])

# Write the results to a CSV file
result_df.to_csv('matching_results.csv', index=False)

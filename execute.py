import pandas as pd

# Load data from Excel file
excel_file = './assets/data.xlsx'
data = pd.read_excel(excel_file)

# Process data (fixing the typo 'revenew')
# Assuming some processing logic here
processed_data = data.to_dict(orient='records')

# Output result to JSON
import json
with open('result.json', 'w') as json_file:
    json.dump(processed_data, json_file, indent=4)

import pandas as pd
import json
import os
import ntpath


# Function to convert CSV to JSON and save to file
def csv_to_json(csv_file):
    # Check if CSV file exists
    if not os.path.exists(csv_file):
        print(f'Error: CSV file "{csv_file}" not found.')
        return

    # Extract filename from CSV file path
    csv_filename = ntpath.basename(csv_file)
    json_file = os.path.splitext(csv_filename)[0] + '.json'

    # Read CSV file into DataFrame
    df = pd.read_csv(csv_file)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records', force_ascii=False, lines=True)

    # Write JSON data to file
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write(json_data)

    print(f'CSV file "{csv_file}" successfully converted to JSON and saved to "{json_file}".')



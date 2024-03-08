import json

# Purpose: Convert a JSON file to a CSV file

def json_to_csv(json_file, csv_file):
    # Open the JSON file and load the data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract the keys from the first dictionary in the JSON
    keys = list(data[0].keys())

    # Open the CSV file in write mode
    with open(csv_file, 'w') as f:
        # Write the header
        f.write(','.join(keys) + '\n')

        # Write the data
        for item in data:
            values = [str(item[key]) for key in keys]
            f.write(','.join(values) + '\n')

# Example usage:
json_file = 'data.json'  # Replace 'data.json' with your JSON file path
csv_file = 'data.csv'    # Replace 'data.csv' with your desired CSV file path
json_to_csv(json_file, csv_file)

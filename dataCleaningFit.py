import json
import pandas as pd
import os
import random

# Define the path to the folder containing the extra Google Fit sleep data files
folder_path = r'C:\Users\tobic\OneDrive\Desktop\Sleep Predictor Data\sleep duration'

# Load the sleep_data_total.csv into a DataFrame
sleep_data_path = r'C:\Users\tobic\OneDrive\Desktop\Sleep Predictor Data\sleep_data_total.csv'
sleep_data = pd.read_csv(sleep_data_path)

# Check if there are any duplicate values in the 'sleep_log_entry_id' column
if sleep_data['sleep_log_entry_id'].duplicated().any():
    print("Duplicate value found!")

# Function to convert seconds to hours
def seconds_to_hours(seconds):
    return round(seconds / 3600, 3)

# Function to generate a unique log_id
def generate_log_id(existing_ids):
    log_id = random.randint(1, 1000000)
    while log_id in existing_ids:
        log_id = random.randint(1, 1000000)
    return log_id

# Collect new rows in a list
new_rows = []

# Process each file in the folder
for entry in os.scandir(folder_path):
    if entry.name.endswith('.json') and entry.is_file():
        print(f"Processing file: {entry.name}")
        with open(entry.path, 'r') as file:
            sleep_data_extra = json.load(file)

        if sleep_data_extra:
            if isinstance(sleep_data_extra, dict):
                end_time = sleep_data_extra['endTime']
            else:
                print("Unexpected format in sleep_data_extra")
                continue
        else:
            print("sleep_data_extra is empty")
            continue

        match = sleep_data['timestamp'] == end_time

        if match.any():
            sleep_data_extra_dict = sleep_data_extra
            if isinstance(sleep_data_extra_dict, dict) and 'duration' in sleep_data_extra_dict:
                duration = sleep_data_extra_dict['duration']
                duration = duration.rstrip('s')
                duration = int(duration)
                duration_sleep_hours = seconds_to_hours(duration)
                if sleep_data.at[match.idxmax(), 'timestamp'] == end_time:
                    sleep_data.loc[match, 'duration_sleep_hours'] = duration_sleep_hours
                    print("Updated row in sleep_data_total.csv")
            else:
                print("Unexpected format in sleep_data_extra")
        else:
            new_row = {
                'sleep_log_entry_id': generate_log_id(set(sleep_data['sleep_log_entry_id'])),
                'timestamp': end_time,
                'overall_score': None,
                'composition_score': None,
                'revitalization_score': None,
                'duration_sleep_hours': duration_sleep_hours,
                'deep_sleep_in_minutes': None,
                'resting_heart_rate': None,
                'restlessness': None
            }
            new_rows.append(new_row)
            print("Generated new row in sleep_data_total.csv")

# Append new rows to the DataFrame
if new_rows:
    new_rows_df = pd.DataFrame(new_rows)
    sleep_data = pd.concat([sleep_data, new_rows_df], ignore_index=True)

# Save the updated DataFrame to a CSV file
sleep_data.to_csv(sleep_data_path, index=False, mode='w')

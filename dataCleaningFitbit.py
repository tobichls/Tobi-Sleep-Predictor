import json
import pandas as pd
import os

# Define the path to the folder containing the extra Fitbit sleep data files
folder_path = r'C:\Users\tobic\OneDrive\Desktop\Sleep Predictor Data\sleep duration fitbit'

# Load the sleep_data_total.csv into a DataFrame
sleep_data_path = r'C:\Users\tobic\OneDrive\Desktop\Sleep Predictor Data\sleep_data_total.csv'
sleep_data = pd.read_csv(sleep_data_path)

# Function to convert minutes to hours
def minutes_to_hours(minutes):
    return round(minutes / 60, 3)

# Process each file in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is a JSON file
    if file_name.endswith('.json'):
        # Construct full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Open and load the JSON file
        with open(file_path, 'r') as file:
            sleep_data_extra = json.load(file)

        # Iterate through each sleep session in the extra data
        for session in sleep_data_extra:
            log_id = session['logId']
            end_time = session['endTime'][:-5]  # Removing milliseconds and timezone for comparison
            minutes_asleep = session['minutesAsleep']
            duration_sleep_hours = minutes_to_hours(minutes_asleep)
            
            # Prepare the match condition
            match_condition = (sleep_data['sleep_log_entry_id'] == log_id) & \
                              (sleep_data['timestamp'].str.startswith(end_time))
            
            # Check if a match is found and update or add new row accordingly
            if sleep_data[match_condition].empty:
                # Add new row
                new_row = {
                    'sleep_log_entry_id': log_id,
                    'timestamp': end_time,
                    'overall_score': None,
                    'composition_score': None,
                    'revitalization_score': None,
                    'duration_sleep_hours': duration_sleep_hours,
                    'deep_sleep_in_minutes': None,
                    'resting_heart_rate': None,
                    'restlessness': None
                }
                sleep_data = pd.concat([sleep_data, pd.DataFrame([new_row])], ignore_index=True)
                print("Added new row to sleep_data_total.csv")
            else:
                # Update existing row
                sleep_data.loc[match_condition, 'duration_sleep_hours'] = duration_sleep_hours
                print("Updated row in sleep_data_total.csv")

# Save the updated DataFrame to a CSV file
sleep_data.to_csv(sleep_data_path, index=False)

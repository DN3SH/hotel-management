import os

# Specify the directory where your JSON files are located
directory_path = "E:\PROJECTS\HOTEL MANAGEMENT SYSTEMS\SAMPLE AADHAR OCR"

# Get a list of JSON files in the directory
json_files = [f for f in os.listdir(directory_path) if f.endswith('.json')]

# Check if there are any JSON files
if json_files:
    # Sort the list by modification time in descending order (most recent first)
    json_files.sort(key=lambda x: os.path.getmtime(os.path.join(directory_path, x)), reverse=True)

    # Get the most recent JSON file
    most_recent_json = json_files[0]
    print("Most recent JSON file:", most_recent_json)
else:
    print("No JSON files found in the directory.")

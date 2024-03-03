import json


#################  Ye code 2 data ko apas me marge krta hy json file me  ############

def merge_json(json_file1, json_file2, merged_json_filename):
    # Load data from the first JSON file
    with open(json_file1, 'r') as f1:
        data1 = json.load(f1)
    
    # Load data from the second JSON file
    with open(json_file2, 'r') as f2:
        data2 = json.load(f2)
    
    # Merge the data from both files
    merged_data = {"route1": data1, "route3": data2}

    # Write the merged data into a new JSON file
    with open(merged_json_filename, 'w') as merged_file:
        json.dump(merged_data, merged_file, indent=4)

    print("Data from both JSON files merged successfully.")

# Names of the JSON files
json_file1 = "coor.json"
json_file2 = "coor3.json"
merged_json_filename = "merged_data.json"  # Choose a name for the merged JSON file

# Merge the data from both JSON files
merge_json(json_file1, json_file2, merged_json_filename)

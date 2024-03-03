import json
import re


####### Ye code data ko fliter krta hy jcy data me koi b symbol ho { \\" } unko 
####### find kr k remove kr ek json formit me covert krta ha  #############

# // ma link nedum kithy jithy he scrape kary   maan ta txt file jy through kayo a neme  merge kr maye ma ink nedum poi lat and lag milda
def txt_to_json(txt_filename, json_filename):
    # TXT file ko read karke data extract karenge
    with open(txt_filename, 'r') as txt_file:
        data = txt_file.read().strip()

    # Data ko appropriate format mein restructure karenge
    json_data = []
    for match in re.finditer(r'\{([^}]*)\}', data):
        temp_dict = {}
        for pair in match.group(1).split(','):
            key, value = pair.split(':')
            temp_dict[key.strip('\\"')] = float(value.strip('\\"'))  # Remove leading and trailing escape characters
        json_data.append(temp_dict)

    # JSON data ko file mein save karenge
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)  # Better readability ke liye indent kiya gaya hai

    print("Data JSON format mein save ho gaya hai.")

# TXT aur JSON files ke liye filenames input lo
txt_filename = "coor3.txt"
json_filename = "coor3.json"

# Convert TXT to JSON
txt_to_json(txt_filename, json_filename)

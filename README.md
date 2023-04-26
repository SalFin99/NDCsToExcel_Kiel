# NDCsToExcel_Kiel


These simple Python functions just clean the JSON dataset and create the "raw" excel file including climate targets and relative level of ambition (if >1)
for every country in it. 

JSON_cleaner opens the json file and removes the following fields for every country:
  - "country_name": "Afghanistan",
  - "region_id": 5,
  - "region_name": "South Asia"
  
The used json file has been already cleaned up by the metadata about authors, contributors, what NDCs are, the description of the various categories of climate targets etc...

Main.py just returns all the excel in the following format:


# NDCsToExcel_Kiel


These simple Python functions just clean the JSON dataset and create the "raw" excel file including climate targets and relative level of ambition (if >1)
for every country in it. 

  
The json files have been already cleaned up by the metadata about authors, contributors, what NDCs are, the description of the various categories of climate targets etc...
Basically the json files start like this:
{
        "AFG": {
            "country_name": "Afghanistan",
            "region_id": 5,
            "region_name": "South Asia",
            "type_of_target": {
                "classification": {
                    "id": 0,
                    "details": "(I)NDC not submitted or not yet included in analysis"
                }
            },
            "temp_target": {
                "classification": {
                    "id": 0,
                    "details": "(I)NDC not submitted or not yet included in analysis"
                }
            },

etc etc

There is no other information, but the data on the states' NDC.


JSON_cleaner opens the json file and removes the following fields for every country:
  - "country_name": "Afghanistan",
  - "region_id": 5,
  - "region_name": "South Asia"


- mergeExcels.py creates a new file merging the excel files of the new and old NDCs.






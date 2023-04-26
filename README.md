# NDCsToExcel_Kiel


These simple Python functions just clean the JSON dataset and create the "raw" excel file including climate targets and relative level of ambition (if >1)
for every country in it. 

JSON_cleaner opens the json file and removes the following fields for every country:
  - "country_name": "Afghanistan",
  - "region_id": 5,
  - "region_name": "South Asia"
  
The used json file has been already cleaned up by the metadata about authors, contributors, what NDCs are, the description of the various categories of climate targets etc...

Main.py just returns all the excel in the following format:

NDC	                       Level
costs of ccm	               4
renewable energy	           3
energy efficiency            3
transport	                   3
agriculture	                 2
land use and forestry	       3
waste	                       3
reducing non co2 gases	     2
fossil fuel subsidiaries	   2
![image](https://user-images.githubusercontent.com/103948003/234531133-56d722b5-1df3-42ce-8136-98ca27405db4.png)



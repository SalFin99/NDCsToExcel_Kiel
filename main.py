import pandas as pd
import JSON_cleaner

data = JSON_cleaner.cleanJSON()

# Loop through each country in the data
for country, country_data in data.items():
    # Create a new pandas DataFrame to hold the data
    df = pd.DataFrame(columns=['Country', 'Category', 'Classification'])

    # Loop through each category in the country
    for category, category_data in country_data.items():
        # Get the name of the category
        category_name = category.replace('_', ' ')
        # Get the classification ID and details
        classification_id = category_data['classification']['id']
        classification_details = category_data['classification']['details']

        if(classification_id>1):
            # Add the data to the DataFrame
            print(country)
            df = pd.concat([df, pd.DataFrame({'Country': [country], 'Category': [category_name], 'Classification': [classification_id]})])

    country_name = country.replace(' ', '_')
    with pd.ExcelWriter('states/' + country_name + '.xlsx') as writer:
        df.to_excel(writer, index=False)



import pandas as pd
import JSON_cleaner

def loadData(cleaned_data):

    data=cleaned_data

    # Loop through each country in the data
    for country, country_data in data.items():
        # Create a new pandas DataFrame to hold the data
        df = pd.DataFrame(columns=['NDC_Old', 'Level'])

    # Loop through each category in the country
        for category, category_data in country_data.items():
        # Get the name of the category
            category_name = category.replace('_', ' ')
        # Get the classification ID and details
            classification_id = category_data['classification']['id']

            if (classification_id > 1):
                df = pd.concat([df, pd.DataFrame({'NDC_Old': [category_name], 'Level': [classification_id]})])

    #return df

        country_name = country.replace(' ', '_')
        with pd.ExcelWriter('baseExcels/' + country_name + '.xlsx') as writer:
            df.to_excel(writer, index=False)

def loadDataNEWndc(cleaned_data):

    data=cleaned_data

    # Loop through each country in the data
    for country, country_data in data.items():
        # Create a new pandas DataFrame to hold the data
        df = pd.DataFrame(columns=['NDC_New', 'Level'])

    # Loop through each category in the country
        for category, category_data in country_data.items():
        # Get the name of the category
            category_name = category.replace('_', ' ')
        # Get the classification ID and details
            classification_id = category_data['classification']['id']

            if (classification_id > 1):
                df = pd.concat([df, pd.DataFrame({'NDC_New': [category_name], 'Level': [classification_id]})])

    #return df

        country_name = country.replace(' ', '_')
        with pd.ExcelWriter('baseExcelsNEW/' + country_name + '.xlsx') as writer:
            df.to_excel(writer, index=False)


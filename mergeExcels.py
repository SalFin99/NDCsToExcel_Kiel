import os
import pandas as pd

def merge_excel_files():
    # Get a list of files in each folder
    files1 = os.listdir('baseExcels')
    files2 = os.listdir('baseExcelsNEW')

    # Find the common filenames
    common_files = set(files1) & set(files2)

    # Create the output folder if it doesn't exist
    os.makedirs('mergedExcels', exist_ok=True)

    # Iterate over the common filenames
    for filename in common_files:
        # Read the Excel files
        file1_path = os.path.join('baseExcels', filename)
        file2_path = os.path.join('baseExcelsNEW', filename)
        df1 = pd.read_excel(file1_path)
        df2 = pd.read_excel(file2_path)

        # Merge the dataframes
        merged_df = pd.concat([df1, df2], axis=1)

        # Write the merged dataframe to a new Excel file
        output_path = os.path.join('mergedExcels', filename)
        merged_df.to_excel(output_path, index=False)

        print(f"Merged file '{filename}' created.")


# Call the merge_excel_files function
merge_excel_files()

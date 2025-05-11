import pandas as pd
import glob
import os
import csv

# summarise csv files in input dir
def summarise_files(input_dir):

    # Dictionary to hold summaries for each file
    file_summaries = {}

    # Get all CSV files in the directory
    csv_files = glob.glob(os.path.join(input_dir, '*.csv'))

    # Process each file
    for file_path in csv_files:

        #  Read file name from path and parse as csv
        file_name = os.path.basename(file_path)
        df = pd.read_csv(file_path)
        
        # Ensure 'Value' column is numeric
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        
        # Drop NaN values in 'Value' and round all values
        df = df.dropna(subset=['Value'])

        # append first and last date to file name
        df["Date Range"] = df['Date'].iloc[-1] + " " + df['Date'].iloc[0]
        
        # Group by 'Category' and sum the 'Value'
        category_totals = df.groupby('Category')['Value'].sum().to_dict()
        
        # Store the result in the dictionary
        file_summaries[file_name] = category_totals

        print("Summarised: " + file_name)
    
    # return the summary dict
    return file_summaries

# write the file summarising the data
def write_summary(output_dir, file_summaries):

    # all unique categories
    all_categories = set()
    for year_data in file_summaries.values():
        all_categories.update(year_data.keys())

    # create rows with above categories
    header = ["Category"] + list(file_summaries.keys())
    rows = []

    # append the values for each category
    for category in sorted(all_categories):
        row = [category]
        for file in file_summaries:
            row.append(file_summaries[file].get(category, 0))
        rows.append(row)

    # write the csv
    with open(output_dir, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

    print("CSV written successfully.")
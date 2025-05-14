import pandas as pd
import glob
import os
import csv

# summarise csv files in input dir
def summarise_files(input_dir):
    file_summaries = {}
    csv_files = glob.glob(os.path.join(input_dir, '*.csv'))
    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        df = pd.read_csv(file_path)
        # format the data
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')           # Ensure 'Value' column is numeric
        df = df.dropna(subset=['Value'])                                    # Drop NaN values in 'Value' and round all values
        df["Date Range"] = df['Date'].iloc[-1] + " " + df['Date'].iloc[0]   # append first and last date to file name
        category_totals = df.groupby('Category')['Value'].sum().to_dict()   # Group by 'Category' and sum the 'Value'
        # Store the result in the dictionary
        file_summaries[file_name] = category_totals
        print("Summarised: " + file_name)
    
    # return the summary dict
    return file_summaries

# write the file summarising the data
def write_summary(output_dir, file_summaries):
    # ensure unique categories
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
        f.close()
    print("CSV written successfully.")
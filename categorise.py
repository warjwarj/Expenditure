import pandas as pd
import os

# This function categorises induvidual transactions using the category_dict
def categorise_transaction(description, category_dict):
    description_lower = description.lower()
    for category, keywords in category_dict.items():
        for keyword in keywords:
            if keyword.lower() in description_lower:
                return category
    return "Uncategorised"

# This loops over files in provided directory and categorises them
def categorise_files(input_dir, output_dir, category_dict):
    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            filepath = os.path.join(input_dir, filename)
            try:
                df = pd.read_csv(filepath)
                if "Description" in df.columns:
                    df["Category"] = df["Description"].apply(lambda x: categorise_transaction(x, category_dict))
                    output_path = os.path.join(output_dir, filename.replace(".csv", "_Categorised.csv"))
                    df.to_csv(output_path, index=False)
                    print(f"Categorised: {filename}")
                else:
                    print(f"Skipped (no 'Description' column): {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
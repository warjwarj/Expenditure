import categorise
import summarise

# raw bank transaction data
raw_data_dir = "./Data/Raw"

# directory to write categorised data to
categorised_data_dir = "./Data/Categorised"

# file to write the summarised data to
summarised_data_file = './Data/Summarised/summary.csv'

# This is used to search for keywords in the description of each transaction
category_dict = {
    "Groceries": ["LIDL", "WAITROSE", "SAINSBURYS", "CO OP"],
    "Food Delivery": ["JUST EAT", "*JUSTEATCOUK", "UBER * EATS", "*UBER EATS", "EATS", "*PMNTSBVEATS"],
    "Fuel": ["SHELL", "ESSO", "PUMP"],
    "Subscriptions": ["PURE GYM LTD", "SPOTIFY", "NETFLIX", "PRIME", "NY TIMES"],
    "Car": ["Halfords", "DVLA VEHICLE TAX", "HASTINGS"],
    "Rent": ["MR AND MRS SJ WARD"],
    "Investments": ["TRADING TWOONETWO", "TRADING 212"]
}

if __name__ == "__main__":

    # categorise the raw transaction data using the keywords above
    categorise.categorise_files(raw_data_dir, categorised_data_dir, category_dict)

    # summarise the categorised data
    summarised_data = summarise.summarise_files(categorised_data_dir)

    # write the summary to a file
    summarise.write_summary(summarised_data_file, summarised_data)
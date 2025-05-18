# expenditure

Summarise your expenditures into categories using bank transaction data.
Add new categories and modify how we classify transactions into categories in the categorisation dictionary.

## Setup

1. Install Python: https://www.python.org/downloads/

2. You need to have bank transaction data to analyse. This is usually downloadable from your online banking provider.

3. In the main.py script adjust the file paths to the  directories containing csv files. The only requirement is having the columns 'Date' and 'Description' in them.

4. Adjust the categorisation dictionary, which looks for keywords and sorts them into categories. The keys are the categories and the values are the keyword arrays.

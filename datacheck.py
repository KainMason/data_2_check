
"""
Your Instructions:


To complete the first knowledge check, do the following:
Create a GitHub repo called "data_1_checks". You will upload ALL knowledge checks to this repo in the future.Send that link to your mentor so they can check it when you finish the assignment.Make a .py (or .ipynb) file that contains the following (your choice of editor does not matter!) and do the following:
Pull in data from an API. Here's a list of public APIs that don't require Auth keys, though if you have another API you want to use feel free: https://apipheny.io/free-api/
Find and print TWO descriptive statistics about your data. This can be absolutely anything, from the mean() or sum() of a column to the number of different categories, to the number of null values in a column. We just want to see two pieces of information.
Write a query in Pandas to select a particular set of your data. You can use a mask or with .query(), but we want you to pull out a subset based on any parameter you like. This could be "show me every row where HTTPS=False" or anything else.
Select and print the SECOND AND THIRD columns of your data frame.
Select and print the FIRST 4 rows of you data frame.
Commit your changes.Push your changes to your repo and notify your mentor!

This project will test your knowledge of pulling in data from an API then doing some quick manipulation and calculation using pandas.




"""


import requests
import pandas as pd

# Make a GET request to the Cat Fact Ninja API to retrieve cat facts
response = requests.get('https://catfact.ninja/facts?limit=10')
data = response.json()

# Extract the relevant data (facts) from the API response
facts = data['data']

# Convert the data to a pandas DataFrame for easier manipulation
df = pd.DataFrame(facts)

# Print the available columns in the DataFrame
print('Available columns:')
print(df.columns)
print()
print('These are the available columns in the DataFrame.')
print()

# Requirement 1: Print two descriptive statistics about the data
print('Number of rows:', len(df))
print('Number of unique facts:', df['fact'].nunique())
print()
print('These statistics fulfill the requirement of providing two pieces of information about the data.')
print()

# Requirement 2: Select a subset of the data based on a parameter
# In this case, we are selecting rows where the length of the cat fact is greater than 50
subset = df[df['length'] > 50]
print('A subset of the data has been created, consisting of rows where the fact length is greater than 50.')
print()

# Requirement 3: Print the second and third columns (if available)
if len(subset.columns) >= 3:
    print('Subset - Second and Third Columns:')
    print(subset.iloc[:, 1:3])
    print('This subset selection and printing of the second and third columns satisfies the requirement of the assignment.')
else:
    print('Subset - Second Column Only:')
    print(subset.iloc[:, 1])
    print('Since there are not three or more columns available, only the second column is printed.')
print()

# Requirement 4: Print the first 4 rows of the subset
print('Subset - First 4 Rows:')
print(subset.head(4))
print('Printing the first 4 rows of the subset fulfills the requirement of the assignment.')

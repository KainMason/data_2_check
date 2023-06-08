import requests
import pandas as pd

# Prompt the user to enter a name
name = input("Enter a name: ")

# Make a GET request to the Gender API
response = requests.get(f"https://api.genderize.io?name={name}")

# Get the JSON data from the response
data = response.json()

# Create a DataFrame with the API response
df = pd.DataFrame(data, index=[0])

# Print two descriptive statistics
print("Descriptive Statistics:")
print("Gender:", df['gender'].values[0])
print("Probability:", df['probability'].values[0])

# Write a query to select a particular set of data
subset = df.query("probability > 0.5")

# Print the second and third columns
print("\nSelected Columns:")
print(subset.iloc[:, 1:3])

# Print the first four rows
print("\nFirst 4 Rows:")
print(df.head(4))

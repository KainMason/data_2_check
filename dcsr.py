import requests
import pandas as pd

# Pull data from the Star Trek API
url = 'http://stapi.co/api/v1/rest/character/search'
query_params = {
    'title': 'captain',
    'limit': 10
}
response = requests.get(url, params=query_params)
data = response.json()

# Create a DataFrame from the character data
characters = data['characters']
df = pd.DataFrame(characters)

# Print two descriptive statistics
character_count = len(df)
species_count = df['species'].nunique()
print("Number of Characters:", character_count)
print("Number of Unique Species:", species_count)

# Select data based on a condition
selected_data = df[df['gender'] == 'male']

# Print the second and third columns
print(selected_data.iloc[:, 1:3])

# Print the first 4 rows
print(selected_data.head(4))

# Commit your changes, push to your GitHub repo, and notify your mentor
# Commit and push code to the GitHub repo "data_1_checks" as instructed.

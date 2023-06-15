import requests
from bs4 import BeautifulSoup

# URL of the Facebook page you want to scrape
url = "https://www.facebook.com/MisterTKMason"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the posts on the page
posts = soup.find_all("div", class_="userContentWrapper")

# List to store offensive posts and their details
offensive_posts = []

# Loop through each post and check for offensive content
for post in posts:
    # Check if the post contains offensive content (add your own offensive content detection logic here)
    if "offensive" in post.text.lower():
        # Get the date of the post
        post_date = post.find("abbr", class_="livetimestamp")["data-utime"]
        
        # Add the offensive post and its details to the list
        offensive_posts.append({
            "content": post.text.strip(),
            "date": post_date
        })

# Print the offensive posts and their details
for post in offensive_posts:
    print("Content:", post["content"])
    print("Date:", post["date"])
    print("-" * 50)

import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import re

########## web scraping scrape only Image to BBC website (03/03/2024)

def validate_filename(filename):
    # Remove all characters that are not letters, numbers, spaces, or underscores
    return re.sub(r'[^\w\s]', '', filename)

# URL of the BBC website
url = 'https://www.bbc.com/news'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Create a directory to save the images
if not os.path.exists('bbc_images'):
    os.makedirs('bbc_images')

# Find all image tags on the page
img_tags = soup.find_all('img')

# Download and save each image
for idx, img in enumerate(img_tags):
    img_url = img['src']
    img_alt = img.get('alt', f'unnamed_{idx}')  # If alt attribute is missing or empty, use unnamed_{idx}
    img_name = f"{validate_filename(img_alt)}.jpg"
    img_path = os.path.join('bbc_images', img_name)
    urllib.request.urlretrieve(img_url, img_path)
    print(f"Downloaded: {img_path}")

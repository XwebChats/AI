from bs4 import BeautifulSoup
from os import system
from requests import *
url = 'http://127.0.0.1:5000'
system('python3 SRVR/app.py')
try:
    response = get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"content:{response.content}")
    # Extract data using appropriate selectors (replace with your specific logic)
    data = []  # Replace with your data extraction logic
except exceptions.RequestException as e:
    print(f"Error fetching data from {url}: {e}")
    print( f"error: \"Failed to scrape data: {e}\"")

from flask import Flask

APP = Flask(__name__)
import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
  """Scrapes title and first paragraph from a Wikipedia page.

  Args:
      url: The URL of the Wikipedia page to scrape.

  Returns:
      A dictionary containing the title and first paragraph, or None if an error occurs.
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-200 status codes

    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1', {'id': 'firstHeading'}).text.strip()
    paragraph = soup.find('div', {'class': 'mw-parser-output'}).find('p').text.strip()

    return {'title': title, 'paragraph': paragraph}
  except requests.exceptions.RequestException as e:
    print(f"Error scraping data from {url}: {e}")
    return None



@APP.route('/')
def index ():
    # Example usage
    page = input("page name: ")
    url = f'https://en.wikipedia.org/wiki/{page}'
    data = scrape_wikipedia(url)
    T = f"Title: {data['title']}"
    P = f"First Paragraph:\n{data['paragraph']}"
    if data:
        print(T)
        print(P)
        return f'{T}\n{P}'
    else:
        print("Error scraping data.")
    
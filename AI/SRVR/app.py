from flask import Flask,render_template

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
    paragraph = soup.find('p',{}).text.strip()

    return {'title': title, 'paragraph': paragraph}
  except requests.exceptions.RequestException as e:
    print(f"Error scraping data from {url}: {e}")
    return None



@APP.route('/')
def index ():
    # Example usage
    return render_template("l.html")    
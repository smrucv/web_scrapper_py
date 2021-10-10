import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    page = requests.get("https://dolartoday.com")
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())

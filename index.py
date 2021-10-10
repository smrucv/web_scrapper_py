import requests
from bs4 import BeautifulSoup

URL = "https://dolartoday.com"

if __name__ == "__main__":
    news = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    news = [{
            "titulo" : new.select_one('div.post-title a')['title'],
            "url" : "".join([URL, new.select_one('div.post-title a')['href']]),
            "img" : new.select_one('div.post-image img')['src']
    } for new in soup.select('.post.type-post') ]
    print(news)

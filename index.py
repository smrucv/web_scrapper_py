import requests
import flask
import json
from bs4 import BeautifulSoup

URL = "https://dolartoday.com"

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    news = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    news = [{
        "titulo": new.select_one('div.post-title a')['title'],
        "url": "".join([URL, new.select_one('div.post-title a')['href']]),
        "img": new.select_one('div.post-image img')['src']
    } for new in soup.select('.post.type-post')]
    return json.dumps(news)

app.run()

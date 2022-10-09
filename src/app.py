from flask import Flask
from urllib.request import urlopen
import json


app = Flask(__name__)


def curl(url):
    page = urlopen(url)
    data_bytes = page.read()
    return data_bytes.decode("utf-8")


@app.route("/")
def index():
    return (
        "Welcome to ScratchDBUpgraded. You can find documentation on the forum thread."
    )


"""

@app.route("/test")
def test():
    return f"Welcome to the testing page"


@app.route("/test/<thing>")
def test2(thing):
    return f"Welcome to the testing page: {thing}"
"""


@app.route("/v1/news/raw")
def v1_news_raw():
    return curl("https://api.scratch.mit.edu/news")


@app.route("/v1/news/<key>")
def v1_news(key):
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)])


@app.route("/v1/news/<key>/id")
def v1_news_id(key):
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["id"])


@app.route("/v1/news/<key>/timestamp")
def v1_news_time(key):
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["stamp"])


@app.route("/v1/news/<key>/title")
def v1_news_title(key):
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["headline"])


@app.route("/v1/news/<key>/url")
def v1_news_url(key):
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["url"])


@app.route("/v1/news/<key>/image_url")
def v1_news_image(key):
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["image"])


@app.route("/v1/news/<key>/description")
def v1_news_desc(key):
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["copy"])

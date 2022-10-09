from flask import Flask
from urllib.request import urlopen
import json
import requests


app = Flask(__name__)


def curl(url):
    page = urlopen(f"https://thingproxy.freeboard.io/fetch/{url}")
    data_bytes = page.read()
    return data_bytes.decode("utf-8")


# Root


@app.route("/")
def index():
    return (
        "Welcome to ScratchDBUpgraded. You can find documentation in the docs folder."
    )


# Login (Broken)

"""
@app.route("/login/<username>/<password>")
def login(username, password):
    headers = {
        "Cookie": "scratchcsrftoken=a; scratchlanguage=en",
        "Origin": "https://scratch.mit.edu",
        "Referer": "https://scratch.mit.edu/",
        "X-CSRFToken": "a",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",
    }
    body = {"useMessages": True, "username": username, "password": password}
    api_endpoint = "https://scratch.mit.edu/accounts/login"
    out = requests.post(url=api_endpoint, headers=headers, b)
    print(out)
    return str(out)
"""

# News


@app.route("/v1/news")
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


# Users
# bio = About me, status = what I'm working on


@app.route("/v1/users/<username>")
def v1_users_raw(username):
    return curl(f"https://api.scratch.mit.edu/users/{username}")

@app.route("/v1/users/<username>/")
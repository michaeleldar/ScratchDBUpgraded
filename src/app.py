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
    try:
        if int(key) < 0 or int(key) > 19:
            return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    except:
        return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)])


@app.route("/v1/news/<key>/id")
def v1_news_id(key):
    try:
        if int(key) < 0 or int(key) > 19:
            return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    except:
        return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["id"])


@app.route("/v1/news/<key>/timestamp")
def v1_news_time(key):
    try:
        if int(key) < 0 or int(key) > 19:
            return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    except:
        return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["stamp"])


@app.route("/v1/news/<key>/title")
def v1_news_title(key):
    try:
        if int(key) < 0 or int(key) > 19:
            return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    except:
        return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["headline"])


@app.route("/v1/news/<key>/url")
def v1_news_url(key):
    try:
        if int(key) < 0 or int(key) > 19:
            return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    except:
        return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["url"])


@app.route("/v1/news/<key>/image_url")
def v1_news_image(key):
    try:
        if int(key) < 0 or int(key) > 19:
            return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    except:
        return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["image"])


@app.route("/v1/news/<key>/description")
def v1_news_desc(key):
    try:
        if int(key) < 0 or int(key) > 19:
            return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    except:
        return "<h3>Error: Key must be a value between 1 and 19, inclusive.</h3>"
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["copy"])


# Users
# bio = About me, status = what I'm working on


@app.route("/v1/users/<username>")
def v1_users_raw(username):
    try:
        return curl(f"https://api.scratch.mit.edu/users/{username}")
    except:
        return "<h3>Error: That username was not found.</h3>"


@app.route("/v1/users/<username>/id")
def v1_users_id(username):
    try:
        data = curl(f"https://api.scratch.mit.edu/users/{username}")
    except:
        return "<h3>Error: That username was not found.</h3>"
    parseable = json.loads(data)
    return str(parseable["id"])


@app.route("/v1/users/<username>/is_scratchteam")
def v1_users_is_scratchteam(username):
    try:
        data = curl(f"https://api.scratch.mit.edu/users/{username}")
    except:
        return "<h3>Error: That username was not found.</h3>"
    parseable = json.loads(data)
    return str(parseable["scratchteam"])


@app.route("/v1/users/<username>/join_date")
def v1_users_join_date(username):
    try:
        data = curl(f"https://api.scratch.mit.edu/users/{username}")
    except:
        return "<h3>Error: That username was not found.</h3>"
    parseable = json.loads(data)
    return str(parseable["history"]["joined"])


# Error Handling


@app.route("/v1/news/raw")
def error410():
    return "<h3>410 Error - This url has been moved to https://ScratchDBUpgraded.applejuicepro.repl.co/v1/news</h3>"


@app.errorhandler(404)
def error404(error):
    return "<h3>404 Error - This url cannot be found. Check it for typos, or go to https://github.com/michaeleldar/ScratchDBUpgraded/tree/master/docs/v1\n for the docs.</h3>"


@app.errorhandler(500)
def error500(error):
    return "<h3>Sorry, it looks like our server malfunctioned. Please go to https://scratch.mit.edu/discuss/topic/634264/ and report what happened there."

from operator import ne
from time import sleep
from urllib.request import urlopen
from os import listdir, system
from random import randint


def curl(url):
    page = urlopen(f"https://thingproxy.freeboard.io/fetch/{url}")
    data_bytes = page.read()
    return data_bytes.decode("utf-8")


def update_db():
    files = listdir("../db")
    for file in files:
        file_formatted = file.replace(".", "/")
        page = curl("https://api.scratch.mit.edu/" + file_formatted)

        file_file = open(f"../db/{file}", "w")
        file_file.write(page)


def get_file(url):
    # url format
    # /news
    url_converted = url.replace("/", ".")
    try:
        if randint(1, 5) == 3:
            raise FileNotFoundError
        file = open("../db/" + url_converted, "r")
        return file.read()
    except FileNotFoundError:
        data = curl("https://api.scratch.mit.edu/" + url)
        system("pwd")
        file = open("../db/" + url_converted, "w")
        file.write(data)
        return data


def continues_update():
    while True:
        sleep(5)
        update_db()

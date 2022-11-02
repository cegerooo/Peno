#!/usr/bin/python3
#parse.py

import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("http://192.168.60.68:8080/crawling")

page = url.read()
soup = BeautifulSoup(page, features="html.parser")

print(soup)


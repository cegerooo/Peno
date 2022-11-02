#!/usr/bin/python3

#parse.py


import re
import urllib3

from urllib.request import urlopen

from bs4 import BeautifulSoup



url = urlopen("http://192.168.60.68:8080/crawling")



page = url.read()

soup = BeautifulSoup(page, features="html.parser")

for link in soup.find_all('a'):
  #print(link.get('href'))
  href="http://192.168.60.68:8080/"+str(link.get('href'))
  url = urlopen(href)
  page = url.read()
  soup = BeautifulSoup(page, features="html.parser")
  print(soup)

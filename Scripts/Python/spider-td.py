#!/usr/bin/python3

#spider.py


import re
import urllib3

from urllib.request import urlopen

from bs4 import BeautifulSoup



url = urlopen("http://192.168.60.68:8080/table")



page = url.read()

soup = BeautifulSoup(page, features="html.parser")

#print(soup.find_all('td'))

td=" "
for value in soup.find_all('td'):
  td=td+str(value).replace("<td>", "").replace("</td>", "").strip()
  td.strip()

print(td)


 # href="http://192.168.60.68:8080/"+str(link.get('href'))
 # url = urlopen(href)
 # page = url.read()
 # soup = BeautifulSoup(page, features="html.parser")
 # print(soup)



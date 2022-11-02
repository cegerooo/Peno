#!/usr/bin/python3
#web-client.py

import requests

url = "http://www.offensive-security.com"

response = requests.get(url)

print("Header:  ")
print("----------")
print(response.headers)

print("Text:    ")
print("----------")
print(response.text)

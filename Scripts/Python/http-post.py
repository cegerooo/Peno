#!/usr/bin/python3
#http-post.py

import requests

url = 'http://192.168.55.68:8080'

info = {'check-key': 'check-value'}
post = requests.post(url, data = info)
print(post.text)

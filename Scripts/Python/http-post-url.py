#!/usr/bin/python3
#http-post.py

import requests

i=0
while i>50:
  url = 'http://192.168.52.68:8080/bijection'
  info = {'check-key': 'check-value'}
  post = requests.post(url, data = info)
  print(post.text)
  i=i+1

#!/usr/bin/python3
#crawl-webserver.py

import requests

Flag="Result:  "
i=1
while i<51:
 url = "http://192.168.60.68:8080/"+str(i)+".html"
 response = requests.get(url)
 Flag=(Flag+response.text).strip()
 i=i+1

print("The Result is:")
print("------------")
print(Flag)

#print("Header:  ")
#print("----------")
#print(response.headers)


#print("Text:    ")
#print("----------")
#print(response.text)


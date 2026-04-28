import requests
from bs4 import BeautifulSoup
url = "https://www.douyu.com"
response=requests.get(url)
response.encoding=response.apparent_encoding
soup=BeautifulSoup(response.text,"html.parser")
title=soup.title.string
print("标题：",title)
#爬标题
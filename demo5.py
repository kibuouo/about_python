import requests
from bs4 import BeautifulSoup

url = "https://www.douyu.com"

# 1. 请求网页
response = requests.get(url)
response.encoding = response.apparent_encoding  # 防止中文乱码

# 2. 解析 HTML
soup = BeautifulSoup(response.text, "html.parser")

# 3. 获取标题
title = soup.title.string

print("网页标题：", title)
import requests
import json
url = "https://api.bilibili.com/x/web-interface/popular"

params = {
    "pn": 1,
    "ps": 20
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, params=params, headers=headers)
data = response.json()
with open("bilibili/popular_videos.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

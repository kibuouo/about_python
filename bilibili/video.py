import requests
import json
url = "https://api.bilibili.com/x/web-interface/view"

params = {
    "bvid": "BV1D1596gEiW"  # 换成真实 BV 号
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, params=params, headers=headers)

data = response.json()

with open("bilibili/video.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

#print(data)

print(data["code"])
print(data["message"])

video = data["data"]

print("标题：", video["title"])
print("UP主：", video["owner"]["name"])
print("播放量：", video["stat"]["view"])
print("点赞：", video["stat"]["like"])
print("投币：", video["stat"]["coin"])
print("收藏：", video["stat"]["favorite"])
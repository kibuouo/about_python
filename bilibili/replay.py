import requests
import json
url = "https://api.bilibili.com/x/v2/reply/wbi/main"

params = {
    "oid": "116571972574050",  
    "type": "1",
    "mode": "3",
    "pagination_str": "",
    "plat": 1,
    "seek_rpid": "",
    "web_location": 1315875,
    "w_rid": "174d2856c79a09ea69a8661beeb88aba",
    "wts": 1778780003
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, params=params, headers=headers)

data = response.json()

with open("bilibili/reply.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

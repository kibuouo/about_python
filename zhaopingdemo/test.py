import requests

url = ""

headers = {
    "User-Agent": "Mozilla/5.0"
}
data = {
    "first": "true",
    "pn": "1",
    "kd": "数据分析"
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text[:500])

json_data = response.json()
print(json_data)
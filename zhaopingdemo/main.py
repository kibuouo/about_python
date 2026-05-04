import requests

def get_html(url):
    headers={
        "User-Agent":"Mozilla/5.0"
        }
    data={
        "first": "true",
        "pn": "1",
        "kd": "数据分析"
    }
    response=requests.post(url,headers=headers,data=data)
    if response.status_code==200:
        return response.json()
    else:
        return response.status_code

if __name__=="__main__":
    url=""
    json=get_html(url)
    print(json)
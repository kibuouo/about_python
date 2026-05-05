import requests
import pandas as pd
import json
import time
url="https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie"
headers={
    "User-Agent":"Mozilla/5.0",
    "Referer":"https://m.douban.com/movie/"
}
movies=[]
datas={}
for start in range(0, 400, 20):
    params={
        "category":"热门",
        "type":"全部",
        "limit":20,
        "start":start
    }
    response=requests.get(url,params=params,headers=headers)
    data=response.json()
    datas.update(data)  
    for item in data["items"]:
        movie={
        "id":item["id"],
        "title":item["title"],
        "rating":item.get("rating", {}).get("value", "N/A"),
        "uri":item["uri"]
        }
        movies.append(movie)
    print(f"已获取 {len(movies)} 条")
    time.sleep(1)
with open("douban_movies.json","w",encoding="utf-8") as f:
    json.dump(datas,f,ensure_ascii=False,indent=4)
df=pd.DataFrame(movies)
hot_df=df[df["rating"]>8.0]
df.to_csv("douban_movies.csv", index=False, encoding="utf-8-sig")
print(hot_df)
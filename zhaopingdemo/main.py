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
all_items = []
for start in range(0, 100, 20):
    params={
        "category":"热门",
        "type":"全部",
        "limit":20,
        "start":start
    }
    response=requests.get(url,params=params,headers=headers)
    response.raise_for_status()
    data=response.json()
    items = data.get("items", []) 
    if not items:
        break
    all_items.extend(items)
    for item in items:
        movie={
        "id":item["id"],
        "title":item["title"],
        "rating":item.get("rating", {}).get("value"),
        "uri":item["uri"],
        "card_subtitle":item.get("card_subtitle", "")
        }
        movies.append(movie)
    print(f"已获取 {len(movies)} 条")
    time.sleep(1)
with open("douban_movies.json","w",encoding="utf-8") as f:
    json.dump(all_items,f,ensure_ascii=False,indent=4)
df=pd.DataFrame(movies)
df["rating"]=pd.to_numeric(df["rating"], errors="coerce")
hot_df=df[df["rating"]>8.0]
df.to_csv("douban_movies.csv", index=False, encoding="utf-8-sig")
print(hot_df)
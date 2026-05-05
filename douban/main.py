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
for start in range(0, 400, 20):
    params={
        "category":"热门",
        "type":"全部",
        "limit":20,
        "start":start
    }
    try:
        response=requests.get(url,params=params,headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"请求失败：{e}")
        continue
    data=response.json()
    items = data.get("items", []) 
    if not items:
        break
    all_items.extend(items)
    for item in items:
        info=item.get("card_subtitle", "")
        parts=info.split("/")
        movie={
        "id":item["id"],
        "title":item["title"],
        "rating":item.get("rating", {}).get("value"),
        "uri":item["uri"],
        #"card_subtitle":item.get("card_subtitle", ""),
        "年份":parts[0].strip() if len(parts) > 0 else "",
        "地区":parts[1].strip() if len(parts) > 1 else "",
        "类型":parts[2].strip() if len(parts) > 2 else "",
        "主演":parts[3].strip() if len(parts) > 3 else ""
        }
        movies.append(movie)
    print(f"已获取 {len(movies)} 条")
    time.sleep(1)
with open("douban_movies_row.json","w",encoding="utf-8") as f:
    json.dump(all_items,f,ensure_ascii=False,indent=4)#原始数据
df=pd.DataFrame(movies)

df.to_csv("douban_clean_movies.csv", index=False, encoding="utf-8-sig")#
type_df=df.copy()
type_df["类型"]=type_df["类型"].str.split()
type_df=type_df.explode("类型")
type_df.to_csv("douban_type_movie.csv",index=False,encoding="utf-8-sig")
country_df=df.copy()
country_df["地区"]=country_df["地区"].str.split(r"\s+")
country_df=country_df.explode("地区")
country_df.to_csv("douban_country_movie.csv",index=False,encoding="utf-8-sig")

df["rating"]=pd.to_numeric(df["rating"], errors="coerce")
hot_df=df[df["rating"]>8.0]

print(hot_df)
print(type_df["类型"].value_counts().head(10))
print(country_df["地区"].value_counts().head(10))
import pandas as pd
import logging
def parse_movies(items):
    logging.info("正在解析电影数据...")
    movies=[]
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
    df=pd.DataFrame(movies)
    df["rating"]=pd.to_numeric(df["rating"], errors="coerce")
    return df
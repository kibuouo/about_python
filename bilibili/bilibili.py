import requests
#import pandas as pd
import json
def get_video_info(bvid):
    
    url = "https://api.bilibili.com/x/web-interface/view"

    params = {
        "bvid": bvid  # 使用传入的 BV 号
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)

    data = response.json()
    with open( "bilibili/video.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    #pd.DataFrame([data]).to_csv("bilibili/video.csv", index=False, encoding="utf-8-sig")
    return data
def get_comments(oid, type=1, mode=3, pagination_str="", plat=1, seek_rpid="", web_location=1315875 ):
    url = "https://api.bilibili.com/x/v2/reply/wbi/main"

    params = {
    "oid": oid,  
    "type": str(type),
    "mode": str(mode),
    "pagination_str": pagination_str,
    "plat": plat,
    "seek_rpid": seek_rpid,
   # "web_location": web_location,
   # "w_rid": "174d2856c79a09ea69a8661beeb88aba",#时间戳签名
   #"wts": "1778780003"#时间戳
}


    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)
    #response.to_csv("bilibili/comments.csv", index=False, encoding="utf-8-sig")
    data = response.json()
    with open("bilibili/comments.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    #pd.DataFrame([data]).to_csv("bilibili/comments.csv", index=False, encoding="utf-8-sig")

    return data
if __name__ == "__main__":
    bvid = "BV1D1596gEiW"  # 替换为你想查询的视频 BV 号
    video_info = get_video_info(bvid)
    oid = video_info["data"]["aid"]  # 替换为你想查询的评论区 oid
    comments_data = get_comments(oid)
    
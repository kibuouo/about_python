import requests
import json
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def get_popular_videos(pn=1, ps=20):
    url = "https://api.bilibili.com/x/web-interface/popular"

    params = {
        "pn": pn,
        "ps": ps
    }   
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, params=params, headers=headers)
    return response.json()
videos=[]
for pn in range(1, 6):#获取前5页的视频数据，每页20条
    logging.info(f"正在获取第 {pn} 页的视频数据...")
    data=get_popular_videos(pn=pn, ps=20)
    video=data["data"]["list"]
    if not video:
        break
    videos.extend(video)
popular_video_info=[]
for video in videos:
    info={
        "视频id": video["bvid"],
        "标题": video["title"],
        "作者": video["owner"]["name"],
        "分区": video["tname"],
        "播放量": video["stat"]["view"],
        "弹幕数": video["stat"]["danmaku"],
        "点赞数": video["stat"]["like"],
        "投币数": video["stat"]["coin"],
        "收藏数": video["stat"]["favorite"],
        "分享数": video["stat"]["share"],
        "评论数": video["stat"]["reply"],
        "时长": video["duration"],
        "发布时间": video["pubdate"]
    }
    popular_video_info.append(info)
with open("bilibili/popular_videos.json", "w", encoding="utf-8") as f:
    json.dump(popular_video_info, f, ensure_ascii=False, indent=4)
df = pd.DataFrame(popular_video_info)#将视频列表转换为DataFrame格式
df.to_csv("bilibili/popular_videos.csv", index=False, encoding="utf-8-sig")#将视频信息保存为CSV文件
df["点赞率"] = df["点赞数"] / df["播放量"] * 100#计算点赞率
df["点赞率显示"] = df["点赞率"].apply(lambda x: f"{x:.2f}%")#将点赞率格式化为百分比字符串  
logging.info("前10个点赞率最高的视频信息：")
top10=df.sort_values(by="点赞率", ascending=False).head(10)[[ "标题", "作者","点赞率显示"]]
logging.info(top10)#输出点赞率最高的前10个视频信息 
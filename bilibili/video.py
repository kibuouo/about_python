import requests
import json
import pandas as pd
import logging
import matplotlib.pyplot as plt
import database as db
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def get_popular_page(pn=1, ps=20):
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
def get_popular_videos(page_count=5, ps=20):
    videos=[]
    for pn in range(1, page_count + 1):#获取前page_count页的视频数据，每页20条
        logging.info(f"正在获取第 {pn} 页的视频数据...")
        data = get_popular_page(pn, ps)
        video = data.get("data", {}).get("list", [])
        if not video:
            break
        videos.extend(video)
    return videos
def parase_video_info(videos):
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
    return popular_video_info
def save_to_json(video_info, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(video_info, f, ensure_ascii=False, indent=4)
def save_to_csv(video_info, filename):
    df = pd.DataFrame(video_info)
    df.to_csv(filename, index=False, encoding="utf-8-sig")
def analyze_video_data(video_info):
    df = pd.DataFrame(video_info)
    df["点赞率"] = df["点赞数"] / df["播放量"] * 100
    df["点赞率显示"] = df["点赞率"].apply(lambda x: f"{x:.2f}%")
    logging.info("前10个点赞率最高的视频信息:")
    top10=df.sort_values(by="点赞率", ascending=False).head(10)[[ "标题", "作者","点赞率显示"]]
    logging.info(top10)
def plot_video_data(video_info):
    # 解决中文乱码
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]#设置字体为微软雅黑
    plt.rcParams["axes.unicode_minus"] = False#解决负号显示问题
    df = pd.DataFrame(video_info)
    top10 = df.sort_values(by="播放量", ascending=False).head(10).copy()
    plt.figure(figsize=(12, 6))
    top10["标题简短"] = top10["标题"].str.slice(0, 6)
    plt.bar(top10["标题简短"], top10["播放量"])#绘制柱状图，x轴为视频标题，y轴为播放量
    plt.ylabel("播放量")
    plt.title("B站热门视频播放量前10")#设置图表标题
    plt.ticklabel_format(style="plain", axis="y")#设置y轴标签格式为plain，避免科学计数法显示
    plt.show()
if __name__ == "__main__":
    videos = get_popular_videos()#获取热门视频数据
    popular_video_info = parase_video_info(videos)#解析视频信息
    db.init_db()
    db.save_to_db(popular_video_info)
    save_to_csv(popular_video_info, "bilibili/popular_videos.csv")#将视频信息保存为CSV文件
    save_to_json(popular_video_info, "bilibili/popular_videos.json")#将视频信息保存为JSON文件
    analyze_video_data(popular_video_info)
    #plot_video_data(popular_video_info)
    

import pandas as pd
import requests
import sqlite3
from pathlib import Path
from flask import Flask, jsonify, render_template, redirect, url_for

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "videos.db"
JSON_PATH = BASE_DIR / "videos.json"

app=Flask(__name__, template_folder=str(BASE_DIR / "templates"))
#获得数据
def get_data():
    url = "https://api.bilibili.com/x/web-interface/popular"
    params = {
        "pn": 1,
        "ps": 20,
    }
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
    }
    response = requests.get(url,params=params, headers=headers)
    return response.json()  
#保存为json
def save_json(videos):
    df=pd.DataFrame(videos)
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        df.to_json(f, orient="records", force_ascii=False, indent=4)
#清洗数据
def parse_data(data):
    videos=[]
    data_list=data.get("data", {}).get("list", [])
    for video in data_list:
        video={
            "title": video.get("title", ""),
            "author": video.get("owner", {}).get("name", ""),
            "view": video.get("stat", {}).get("view", 0),
            "bvid": video.get("bvid", ""),
        }
        videos.append(video)
    return videos
#保存到数据库
def save_sql(videos):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bvid TEXT UNIQUE,
            title TEXT,
            author TEXT,
            view INTEGER
        )
    """)
    for video in videos:
        cursor.execute("""
            INSERT OR REPLACE INTO videos (bvid, title, author, view) VALUES (?, ?, ?, ?)
        """, (video["bvid"], video["title"], video["author"], video["view"]))
    conn.commit()
    conn.close()
#查询数据库
def query():
    conn=sqlite3.connect(DB_PATH)
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()
    cursor.execute("SELECT title, author, view FROM videos")
    videos=[dict(video) for video in cursor.fetchall()]
    conn.close()
    return videos
#分析数据
def get_view(video):
    return video["view"]
def analysis_data(videos):
    top1=max(videos,key=get_view)
    print(f"观看量最高的视频是：{top1['title']}，作者是{top1['author']}，观看量是{top1['view']}")
def create_app():
    
    @app.route("/")
    def index():
        videos=query()
        return render_template("index.html", videos=videos)

    return app
def main():
    data=get_data()
    videos=parse_data(data)
    save_json(videos)
    save_sql(videos)
    analysis_data(videos)
    create_app()

if __name__ == "__main__":
    main()
    app.run(debug=True)

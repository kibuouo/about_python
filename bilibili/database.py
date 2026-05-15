import sqlite3


def init_db(db_path="bilibili/data/bilibili.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS popular_videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bvid TEXT UNIQUE,
            title TEXT,
            author TEXT,
            category TEXT,
            view_count INTEGER,
            danmaku_count INTEGER,
            like_count INTEGER,
            coin_count INTEGER,
            favorite_count INTEGER,
            share_count INTEGER,
            reply_count INTEGER,
            duration INTEGER,
            pubdate INTEGER,
            like_rate REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
def save_to_db(video_info, db_path="bilibili/data/bilibili.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for video in video_info:
        like_rate = video["点赞数"] / video["播放量"] if video["播放量"] != 0 else 0

        cursor.execute("""
            INSERT OR REPLACE INTO popular_videos (
                bvid,
                title,
                author,
                category,
                view_count,
                danmaku_count,
                like_count,
                coin_count,
                favorite_count,
                share_count,
                reply_count,
                duration,
                pubdate,
                like_rate
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            video["视频id"],
            video["标题"],
            video["作者"],
            video["分区"],
            video["播放量"],
            video["弹幕数"],
            video["点赞数"],
            video["投币数"],
            video["收藏数"],
            video["分享数"],
            video["评论数"],
            video["时长"],
            video["发布时间"],
            like_rate
        ))

    conn.commit()
    conn.close()
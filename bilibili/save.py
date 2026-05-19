"""数据保存模块：支持 JSON、CSV 和 SQLite"""

import json
import logging

import pandas as pd

import database as db


def save_to_json(video_info, filename="bilibili/data/popular_videos.json"):
    """保存为 JSON 文件"""
    logging.info(f"正在保存到 JSON: {filename}")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(video_info, f, ensure_ascii=False, indent=4)


def save_to_csv(video_info, filename="bilibili/data/popular_videos.csv"):
    """保存为 CSV 文件"""
    logging.info(f"正在保存到 CSV: {filename}")
    df = pd.DataFrame(video_info)
    df.to_csv(filename, index=False, encoding="utf-8-sig")


def save_all(video_info):
    """统一保存：JSON + CSV + 数据库"""
    db.init_db()
    db.save_to_db(video_info)
    save_to_json(video_info)
    save_to_csv(video_info)

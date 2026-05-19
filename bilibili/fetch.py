"""数据获取模块：请求 B站热门视频 API"""

import requests
import logging


def get_popular_page(pn=1, ps=20):
    """获取单页热门视频"""
    url = "https://api.bilibili.com/x/web-interface/popular"
    params = {
        "pn": pn,
        "ps": ps,
    }
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


def get_popular_videos(page_count=5, ps=20):
    """获取前 page_count 页的热门视频列表"""
    videos = []
    for pn in range(1, page_count + 1):
        logging.info(f"正在获取第 {pn} 页的视频数据...")
        data = get_popular_page(pn, ps)
        video_list = data.get("data", {}).get("list", [])
        if not video_list:
            break
        videos.extend(video_list)
    return videos

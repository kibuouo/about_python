"""数据解析模块：将原始 JSON 转为结构化字典列表"""

import logging


def parse_video_info(videos):
    """解析视频原始数据，提取关键字段"""
    logging.info("正在解析视频数据...")
    popular_video_info = []
    for video in videos:
        info = {
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
            "发布时间": video["pubdate"],
        }
        popular_video_info.append(info)
    return popular_video_info

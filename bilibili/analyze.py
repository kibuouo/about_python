"""数据分析与可视化模块"""

import logging

import matplotlib.pyplot as plt
import pandas as pd


def analyze_video_data(video_info):
    """分析视频数据，输出点赞率前10"""
    df = pd.DataFrame(video_info)
    df["点赞率"] = df["点赞数"] / df["播放量"] * 100
    df["点赞率显示"] = df["点赞率"].apply(lambda x: f"{x:.2f}%")

    logging.info("前10个点赞率最高的视频信息:")
    top10 = df.sort_values(by="点赞率", ascending=False).head(10)[
        ["标题", "作者", "点赞率显示"]
    ]
    logging.info(top10)
    return df


def plot_video_data(video_info):
    """绘制播放量前10的柱状图"""
    # 解决中文乱码
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
    plt.rcParams["axes.unicode_minus"] = False

    df = pd.DataFrame(video_info)
    top10 = df.sort_values(by="播放量", ascending=False).head(10).copy()

    plt.figure(figsize=(12, 6))
    top10["标题简短"] = top10["标题"].str.slice(0, 6)
    plt.bar(top10["标题简短"], top10["播放量"])
    plt.ylabel("播放量")
    plt.title("B站热门视频播放量前10")
    plt.ticklabel_format(style="plain", axis="y")
    plt.show()

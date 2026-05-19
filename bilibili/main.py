"""主入口：编排 B站热门视频数据采集全流程"""

import logging

from fetch import get_popular_videos
from parse import parse_video_info
from save import save_all
from analyze import analyze_video_data, plot_video_data


def main():
    """执行完整的数据采集 → 解析 → 保存 → 分析流程"""
    # 1. 获取数据
    videos = get_popular_videos()

    # 2. 解析数据
    video_info = parse_video_info(videos)

    # 3. 保存数据（JSON + CSV + SQLite）
    save_all(video_info)

    # 4. 分析数据
    analyze_video_data(video_info)

    # 5. 可视化（如需显示图表请取消注释）
    # plot_video_data(video_info)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    main()

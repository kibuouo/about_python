#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 电影数据保存模块
# 功能：将电影数据列表保存为CSV格式文件
# 依赖：csv (标准库)

import csv  # 导入csv模块


def savetocsv(movie_list, filename):
    # 将电影列表保存为CSV文件
    # 参数：movie_list - 电影字典列表，filename - CSV文件名
    with open(filename,"w",encoding="utf-8-sig",newline="")as f:  # 打开文件，UTF-8编码
        writer = csv.DictWriter(f,fieldnames=["title","score"])  # 创建CSV写入器
        writer.writeheader()  # 写入表头
        for movie in movie_list:  # 遍历每部电影
            writer.writerow(movie)  # 写入电影数据
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 电影数据HTML解析模块
# 功能：使用BeautifulSoup解析HTML，提取电影标题和评分
# 依赖：bs4 (BeautifulSoup)

from bs4 import BeautifulSoup  # 导入BeautifulSoup库


def parser_movie(html):
    # 解析HTML页面，提取电影信息
    # 参数：html - 网页HTML内容
    # 返回：电影字典列表，每项包含title和score
    soup = BeautifulSoup(html,"html.parser")  # 创建BeautifulSoup对象
    movie_list=[]  # 初始化电影列表
    items = soup.find_all("div",class_="el-card")  # 查找所有电影卡片
    for item in items:  # 遍历每个电影项
        title_tag = item.find("h2")  # 查找标题标签
        score_tag = item.find("p",class_="score")  # 查找评分标签
        if title_tag:  # 判断标题是否存在
            title=title_tag.text.strip()  # 提取标题文本
        else:
            title="未知标题"  # 默认标题
        if score_tag:  # 判断评分是否存在
            score=score_tag.text.strip()  # 提取评分文本
        else:
            score="无评分"  # 默认评分
        movie={
            "title":title,  # 电影标题
            "score":score   # 电影评分
        }
        movie_list.append(movie)  # 添加到电影列表
    return movie_list  # 返回电影列表